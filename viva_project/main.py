from image_processing import analyze_image
from speech_recognition_util import get_speech_input
from openai_client import get_openai_response
import pyttsx3

def main():
    """Função principal que coordena o fluxo do programa."""
    engine = pyttsx3.init()
    while True:
        user_input = get_speech_input(engine)

        if 'analisar imagem' in user_input.lower():
            analyze_image(engine)
            continue

        if user_input == "":
            continue

        response = get_openai_response(user_input)
        mensagem = response.content
        print("Resposta:", mensagem)

        engine.say(mensagem)
        engine.runAndWait()

        if 'encerrar' in user_input.lower():
            mensagem = "Encerrando o chat."
            print(mensagem)
            engine.say(mensagem)
            engine.runAndWait()
            break

if __name__ == "__main__":
    main()
