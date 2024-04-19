import requests
from bs4 import BeautifulSoup
import nltk
import re

def extraer_texto_pagina(url):
    try:
        # Realizar la solicitud GET a la página web
        respuesta = requests.get(url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Crear un objeto BeautifulSoup para analizar el contenido HTML
            soup = BeautifulSoup(respuesta.content, 'html.parser')
            # Extraer el texto del cuerpo de la página
            texto = soup.get_text()
            return texto
        else:
            print("Error al solicitar la página:", respuesta.status_code)
            return None
    except requests.RequestException as e:
        print("Error de solicitud:", e)
        return None

def main():
    # Pedir al usuario la URL de la página web
    url = input("Introduce la URL de la página web: ")
    # Extraer el texto de la página web
    texto_pagina = extraer_texto_pagina(url)
    if texto_pagina:
        # Guardar el texto en un archivo de texto "pagina.txt"
        with open("pagina.txt", "w", encoding="utf-8") as archivo:
            archivo.write(texto_pagina)
        print("El archivo se ha creado correctamente.")

        # Cargar el texto del archivo
        archivo_nombre = "pagina.txt"
        with open(archivo_nombre, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        print("----------------------------------------------------------------------")

        # Contar el número de palabras en la página
        num_palabras = len(re.findall(r'\w+', texto))
        print("Número de palabras en la página:", num_palabras)

        # Contar el número de líneas de texto en la página
        num_lineas = texto.count('\n')
        print("Número de líneas de texto en la página:", num_lineas)

        print("----------------------------------------------------------------------")

        # Mostrar palabras de 3 o 4 caracteres
        palabras_3_4 = re.findall(r'\b\w{3,4}\b', texto)
        print("Palabras de 3 o 4 caracteres:", palabras_3_4)

        print("----------------------------------------------------------------------")

        # Contar el número de veces que aparece una palabra fija en el texto
        palabra_fija = "ustedes"  # Palabra fija a contar
        num_apariciones = texto.lower().count(palabra_fija.lower())
        print(f"Número de veces que aparece la palabra '{palabra_fija}': {num_apariciones}")

        print("----------------------------------------------------------------------")

        # Cargar palabras funcionales en español de NLTK
        palabras_funcionales = nltk.corpus.stopwords.words("spanish")
        for palabras_funcional in palabras_funcionales:
            print(palabras_funcional)

        print("----------------------------------------------------------------------")

        # Tokenizar el texto y eliminar palabras funcionales
        tokens = nltk.word_tokenize(texto, "spanish")
        tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

        # Imprimir algunos detalles sobre los tokens
        print(tokens_limpios)
        print("Número total de tokens:", len(tokens))
        print("Número de tokens limpios:", len(tokens_limpios))

        # Crear un objeto Text de NLTK y calcular la distribución de frecuencia
        texto_limpio_nltk = nltk.Text(tokens_limpios)
        distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

        # Graficar las 40 palabras más comunes
        distribucion_limpia.plot(40)
    else:
        print("No se pudo extraer el texto de la página web.")

if __name__ == "__main__":
    main()
