import speech_recognition as sr

def get_speech_input(engine):
    """Captura a entrada de fala do usuário e retorna o texto reconhecido."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        mensagem = "Aguardando sua fala..."
        print(mensagem)
        engine.say(mensagem)
        engine.runAndWait()

        audio = recognizer.listen(source)

    try:
        print("Reconhecendo fala...")
        texto = recognizer.recognize_google(audio, language="pt-BR")
        mensagem = f"Você disse: {texto}"
        print(mensagem)
        engine.say(mensagem)
        engine.runAndWait()
        return texto
    except sr.UnknownValueError:
        mensagem = "Não entendi o que você disse."
        print(mensagem)
        engine.say(mensagem)
        engine.runAndWait()
        return ""
    except sr.RequestError:
        mensagem = "Erro ao se comunicar com o serviço de reconhecimento de fala."
        print(mensagem)
        engine.say(mensagem)
        engine.runAndWait()
        return ""
