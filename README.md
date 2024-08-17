# Viva-Vision 🌟

## O que é o projeto

**Viva-Vision** é um projeto inovador de Inteligência Artificial voltado para a acessibilidade, especialmente para pessoas com deficiência visual. Este sistema utiliza reconhecimento de imagem para fornecer descrições detalhadas do ambiente ao redor do usuário, através de uma câmera conectada a um alto-falante. Além de descrever cenários em tempo real, o Viva-Vision também funciona como um chatbot generativo, permitindo uma interação mais rica e informativa. 📷🔊

## Por que essa escolha

A escolha deste projeto é motivada pela necessidade de oferecer mais autonomia e qualidade de vida para pessoas com deficiência visual. Com o Viva-Vision, queremos proporcionar uma maneira de "enxergar" o mundo ao redor, utilizando tecnologia de ponta para descrever o ambiente e permitir interações significativas através de conversas. 🌍💬

## Como pode ajudar

O Viva-Vision permite que pessoas com deficiência visual obtenham descrições detalhadas e precisas do que está acontecendo ao seu redor em tempo real. Isso ajuda a melhorar a percepção espacial e a compreensão do ambiente, oferecendo uma ferramenta poderosa para aumentar a autonomia e a integração social. Além disso, a função de chatbot generativo permite interações conversacionais que enriquecem ainda mais a experiência do usuário. 🌟🤖

## Tecnologias Utilizadas

- **Reconhecimento de Imagem**: Utiliza o modelo BLIP para gerar descrições das imagens capturadas pela câmera. 🖼️
- **Processamento de Linguagem Natural (NLP)**: Utiliza a OpenAI API para gerar respostas conversacionais. 🧠
- **Tradução**: Google Translator é usado para traduzir as descrições para o idioma desejado. 🌐
- **Síntese de Fala**: Pyttsx3 para converter texto em fala e fornecer feedback auditivo ao usuário. 🎙️
- **Reconhecimento de Fala**: SpeechRecognition para captar e interpretar comandos de voz. 🎤

## Requisitos

- **Python 3.7+** 🐍
- **Bibliotecas Python**:
  - OpenCV 📸
  - Pillow 🖼️
  - deep_translator 🌐
  - pyttsx3 🎙️
  - transformers 🤖
  - openai 🌟
  - SpeechRecognition 🎤

## Como Funciona

1. **Inicialização**:
   - O código inicializa o cliente da OpenAI, o motor de síntese de voz, e o tradutor. ⚙️

2. **Carregamento do Modelo**:
   - Carrega o modelo BLIP para descrição de imagens. 📚

3. **Análise de Imagem**:
   - Captura imagens da câmera, gera uma legenda para a imagem, traduz a descrição e a reproduz em voz alta. 📷➡️📝🔊

4. **Reconhecimento de Fala**:
   - Capta o áudio do usuário, reconhece a fala e responde com base no comando recebido. 🎤➡️🗣️

5. **Interação com o Chatbot**:
   - Envia perguntas para o modelo da OpenAI e reproduz as respostas em voz alta. 💬🔄🔊

## Como Contribuir

Contribuições são bem-vindas! Se você deseja colaborar com o Viva-Vision, siga estas etapas:

1. Faça um fork do repositório. 🍴
2. Crie uma branch para suas alterações. 🌿
3. Realize suas modificações e adicione testes, se necessário. 🛠️
4. Envie um pull request com uma descrição detalhada das mudanças. 🚀

## Uso

Para executar o Viva-Vision:

1. Instale as dependências necessárias:
   ```bash
   pip install opencv-python Pillow deep-translator pyttsx3 transformers openai SpeechRecognition
