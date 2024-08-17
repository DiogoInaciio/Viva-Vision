import cv2
from PIL import Image
from deep_translator import GoogleTranslator
import pyttsx3
import gc
import time
from transformers import BlipProcessor, BlipForConditionalGeneration
from openai import OpenAI  # pip install openai
import speech_recognition as sr  # pip install SpeechRecognition

# Inicializa o cliente OpenAI
client = OpenAI(api_key="nada", base_url="http://localhost:11434/v1/")

# Inicialização do motor de síntese de voz
engine = pyttsx3.init()

# Inicialização do tradutor
tradutor = GoogleTranslator(source="en", target="pt")

# Função para carregar o modelo BLIP
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    return processor, model

processor, model = load_model()
prompt = ""

def resize_image(image, max_size=800):
    width, height = image.size
    if max(width, height) > max_size:
        scale = max_size / float(max(width, height))
        return image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
    return image

def analyze_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        message = "Erro ao abrir a câmera."
        print(message)
        engine.say(message)
        engine.runAndWait()
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            message = "Erro ao capturar a imagem."
            print(message)
            engine.say(message)
            engine.runAndWait()
            break

        frame = cv2.resize(frame, (640, 480))  # Reduz a resolução do frame
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Redimensionar a imagem se necessário
        image = resize_image(image)

        # Processar e gerar a legenda
        inputs = processor(images=image, text=prompt, return_tensors="pt")
        out = model.generate(**inputs)
        generated_text = processor.decode(out[0], skip_special_tokens=True)

        # Traduzir a legenda
        traducao = tradutor.translate(generated_text)
        print("Legenda gerada:", traducao)

        # Sintetizar a fala
        engine.say(traducao)
        engine.runAndWait()

        # Libere recursos não utilizados
        del image, inputs, out, generated_text, traducao, frame
        gc.collect()

        cap.release()
        cv2.destroyAllWindows()
        break  # Encerrar após uma análise de imagem

def get_speech_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        message = "Aguardando sua fala..."
        print(message)
        engine.say(message)
        engine.runAndWait()

        audio = recognizer.listen(source)

    try:
        print("Reconhecendo fala...")
        text = recognizer.recognize_google(audio, language="pt-BR")
        message = f"Você disse: {text}"
        print(message)
        engine.say(message)
        engine.runAndWait()
        return text
    except sr.UnknownValueError:
        message = "Não entendi o que você disse."
        print(message)
        engine.say(message)
        engine.runAndWait()
        return ""
    except sr.RequestError:
        message = "Erro ao se comunicar com o serviço de reconhecimento de fala."
        print(message)
        engine.say(message)
        engine.runAndWait()
        return ""

# Função principal
def main():
    while True:
        # Solicita a pergunta do usuário via fala
        user_input = get_speech_input()

        # Verifica se o usuário quer encerrar o chat
        if 'analisar imagem' in user_input.lower():
            analyze_image()
            continue  # Volta ao início do loop após análise de imagem

        if user_input == "":
            continue  # Tenta novamente caso o reconhecimento falhe

        # Envia a pergunta para o modelo
        response = client.chat.completions.create(
            model="llama3",
            messages=[
                {"role": "user", "content": user_input}
            ],
            stream=False
        )

        # Exibe a resposta do modelo
        message = response.choices[0].message.content
        print("Resposta:", message)

        # Sintetizar a resposta do modelo
        engine.say(message)
        engine.runAndWait()

        # Verifica se o usuário deseja encerrar o chat
        if 'encerrar' in user_input.lower():
            message = "Encerrando o chat."
            print(message)
            engine.say(message)
            engine.runAndWait()
            break

if __name__ == "__main__":
    main()
