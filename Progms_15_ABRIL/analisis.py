import requests
from bs4 import BeautifulSoup

# URL de la página web que quieres analizar
url = 'https://www.fotogramas.es/noticias-cine/a46955383/kung-fu-panda-4-sinopsis-reparto-trailer/'

# Realizar la solicitud GET a la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener el contenido HTML de la página
    html = response.content
    
    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Encontrar y extraer el texto de todos los elementos <p> (párrafos) en la página
    paragraphs = soup.find_all('p')
    
    # Imprimir el texto de cada párrafo
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print('Error al cargar la página:', response.status_code)
