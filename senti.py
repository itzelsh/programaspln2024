# Instalar las bibliotecas necesarias
#pip install sentiment-analysis-spanish
#pip install keras tensorflow

from sentiment_analysis_spanish import sentiment_analysis

# Crear una instancia del analizador de sentimientos
analizador = sentiment_analysis.SentimentAnalysisSpanish()

def interpretar_sentimiento(puntuacion):
    if puntuacion > 0.6:
        return "positivo"
    elif puntuacion < 0.4:
        return "negativo"
    else:
        return "neutral"

# Pedir al usuario que ingrese una frase
frase = input("Por favor, ingresa una frase para analizar su sentimiento: ")

# Analizar el sentimiento de la frase ingresada
puntuacion = analizador.sentiment(frase)
sentimiento = interpretar_sentimiento(puntuacion)

# Imprimir el resultado
print(f"Texto: '{frase}'")
print(f"Sentimiento: {sentimiento}\n")

