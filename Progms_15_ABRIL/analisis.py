import requests
from bs4 import BeautifulSoup
from collections import Counter

# Función para obtener el texto de una página web y encontrar la palabra más común
def encontrar_palabra_mas_comun(url):
    # Realizar la solicitud GET a la página web
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener el contenido HTML de la página
        html = response.content
        
        # Crear un objeto BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extraer el texto de la página
        text = soup.get_text()
        
        # Tokenizar el texto en palabras individuales
        words = text.split()
        
        # Contar la frecuencia de cada palabra
        word_counts = Counter(words)
        
        # Encontrar la palabra más común
        most_common_word = word_counts.most_common(1)[0][0]
        
        # Resaltar la palabra más común en el texto
        highlighted_text = text.replace(most_common_word, f"\033[1m{most_common_word}\033[0m")
        
        return highlighted_text
    else:
        return 'Error al cargar la página: {}'.format(response.status_code)

# Solicitar al usuario la dirección de la página web
url = input("Ingresa la dirección URL de la página web que deseas analizar: ")

# Obtener el texto de la página web y encontrar la palabra más común
texto_resaltado = encontrar_palabra_mas_comun(url)

# Imprimir el texto resaltado
print(texto_resaltado)
