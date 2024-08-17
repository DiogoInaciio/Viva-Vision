import cv2
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from translation import tradutor
import gc

BLIP_MODEL_NAME = "Salesforce/blip-image-captioning-base"
MAX_IMAGE_SIZE = 800

def load_model():
    """Carrega o modelo BLIP para geração de legendas."""
    processor = BlipProcessor.from_pretrained(BLIP_MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(BLIP_MODEL_NAME)
    return processor, model

processor, model = load_model()

def resize_image(image, max_size=MAX_IMAGE_SIZE):
    """Redimensiona a imagem para garantir que não exceda o tamanho máximo."""
    width, height = image.size
    if max(width, height) > max_size:
        scale = max_size / float(max(width, height))
        return image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
    return image

def analyze_image(engine):
    """Captura uma imagem da câmera, gera e traduz uma legenda, e a lê em voz alta."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        mensagem = "Erro ao abrir a câmera."
        print(mensagem)
        engine.say(mensagem)
        engine.runAndWait()
        return

    ret, frame = cap.read()
    if not ret:
        mensagem = "Erro ao capturar a imagem."
        print(mensagem)
        engine.say(mensagem)
        engine.runAndWait()
        cap.release()
        cv2.destroyAllWindows()
        return

    frame = cv2.resize(frame, (640, 480))
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image = resize_image(image)

    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    generated_text = processor.decode(out[0], skip_special_tokens=True)

    traducao = tradutor.translate(generated_text)
    print("Legenda gerada:", traducao)

    engine.say(traducao)
    engine.runAndWait()

    del image, inputs, out, generated_text, traducao, frame
    gc.collect()

    cap.release()
    cv2.destroyAllWindows()
