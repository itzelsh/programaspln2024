import nltk
import os
from PyPDF2 import PdfReader

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_lineas(texto):
    lineas = texto.split('\n')
    return len(lineas)

def contar_apariciones(texto, palabra):
    return texto.count(palabra)

def main():
    while True:
        # Pedir al usuario el nombre del archivo PDF
        archivo_pdf = input("Por favor, ingresa el nombre del archivo PDF (sin la extensión): ")

        # Agregar la extensión .pdf al nombre del archivo
        archivo_pdf += ".pdf"

        # Verificar si el archivo existe
        if not os.path.isfile(archivo_pdf):
            print("El archivo especificado no existe.")
            continuar = input("¿Deseas intentarlo de nuevo? (s/n): ").lower()
            if continuar != "s":
                break
            else:
                continue

        try:
            # Leer el documento PDF
            with open(archivo_pdf, 'rb') as archivo:
                lector_pdf = PdfReader(archivo)
                texto = ''
                for pagina in lector_pdf.pages:
                    texto += pagina.extract_text()

            # Escribir el texto extraído en un archivo de texto .txt
            with open("texto_extraido.txt", "w", encoding="utf-8") as archivo_txt:
                archivo_txt.write(texto)

            print("Texto extraído correctamente y guardado en 'texto_extraido.txt'.")

            print("----------------------------------------------------------------------")

            # Cargar palabras funcionales en español de NLTK
            nltk.download("stopwords")
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

            # Graficar las 20 palabras más comunes
            distribucion_limpia.plot(20)

            # Contar palabras y líneas
            num_palabras = contar_palabras(texto)
            num_lineas = contar_lineas(texto)

            # Contar apariciones de la palabra buscada
            palabra_buscada = input("Por favor, ingresa la palabra que deseas buscar en el texto: ")
            num_apariciones = contar_apariciones(texto, palabra_buscada)

            # Imprimir resultados
            print("Número de palabras en el documento:", num_palabras)
            print("Número de líneas de texto en el documento:", num_lineas)
            print("Número de veces que aparece la palabra '{}' en el documento:".format(palabra_buscada), num_apariciones)

            # Preguntar al usuario si desea continuar
            continuar = input("¿Deseas continuar? (s/n): ").lower()
            if continuar != "s":
                break

        except Exception as e:
            print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
