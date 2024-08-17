from openai import OpenAI

API_KEY = "nada"
BASE_URL = "http://localhost:11434/v1/"
MODEL_NAME = "llama3"

# Inicializa o cliente OpenAI
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def get_openai_response(user_input):
    """Envia a entrada do usuário para o modelo OpenAI e retorna a resposta."""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": user_input}
        ],
        stream=False
    )
    return response.choices[0].message
