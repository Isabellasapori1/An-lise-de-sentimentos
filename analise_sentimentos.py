from textblob import TextBlob
from googletrans import Translator

def analisar_sentimento():
    print("Bem-vindo ao Analisador de Sentimentos!")
    print("Digite uma frase e veja se ela é positiva, negativa ou neutra.\n")
    
    translator = Translator()
    
    while True:
        texto = input("Digite um texto (ou 'sair' para encerrar): ")
        if texto.lower() == 'sair':
            print("Encerrando o programa. Até logo!")
            break
        
        # Traduz o texto para inglês
        traduzido = translator.translate(texto, src='pt', dest='en').text
        print(f"Texto traduzido: {traduzido}")

        # Analisa o sentimento do texto traduzido
        blob = TextBlob(traduzido)
        sentimento = blob.sentiment.polarity

        if sentimento > 0:
            print("Sentimento Positivo 😊")
        elif sentimento < 0:
            print("Sentimento Negativo 😟")
        else:
            print("Sentimento Neutro 😐")
        print("-" * 50)

if __name__ == "__main__":
    analisar_sentimento()

