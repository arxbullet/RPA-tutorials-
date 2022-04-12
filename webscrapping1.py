import requests #gestiona peticiones http para obtener pag web
from bs4 import BeautifulSoup as b #extraer o gestionar info de pag web


url='https://www.pcfactory.cl/'

html = requests.get(url)
content = html.content
soup = b(content, 'html') 

categoria = soup.find("a", {"class":"link link--bold color-primary-2"})
#encontrar un elemento en la pagina actual con beutifull soup
print(categoria)

