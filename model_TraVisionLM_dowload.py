from transformers import AutoModelForCausalLM, AutoProcessor
import requests
from PIL import Image
from io import BytesIO

# Carregar o modelo e o processor
model = AutoModelForCausalLM.from_pretrained('ucsahin/TraVisionLM-base', trust_remote_code=True, device_map="cpu")
processor = AutoProcessor.from_pretrained('ucsahin/TraVisionLM-base', trust_remote_code=True)

# Baixar e carregar a imagem
url = "https://images.pexels.com/photos/109919/pexels-photo-109919.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260"
response = requests.get(url)
if response.status_code == 200:
    image = Image.open(BytesIO(response.content)).convert("RGB")
else:
    raise Exception(f"Failed to download image. Status code: {response.status_code}")

# Definir o prompt
prompt = "Açıkla"  # short caption

# Processar a entrada
inputs = processor(text=prompt, images=image, return_tensors="pt").to("cpu")

# Gerar a saída
outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, temperature=0.6, top_p=0.9, top_k=50, repetition_penalty=1.2)

# Decodificar e imprimir a saída
output_text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
print("Model response: ", output_text)
