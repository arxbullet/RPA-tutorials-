# install pillow
from PIL import Image
import io
import requests 
from bs4 import BeautifulSoup as b 
import win32api
# algunas paginas identifican el scrapping, y ocultan la informacion, 
# para obtener los datos en ese caso, al metodo request debemos pasarle las cabeceras de la peticion
# para obtener las cabeceras, debemos ir a network en inspeccionar, headers
# headers = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#   'Accept-Encoding': 'gzip, deflate, br'
#   'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8'
#   'Connection': 'keep-alive'}
# html = requests.get(url, headers= headers)

url='https://www.pcfactory.cl/smartphones?categoria=5&papa=645'
path_photos = ''

html = requests.get(url)
content = html.content
soup = b(content, 'html') 
i = 1 #variable para ir contando cuantas fotos van
categorias = soup.findAll("div", {"class":"product"})

for categoria in categorias:

    marca = categoria.find("div", {"class":"card-title color-dark"}).text
    id = categoria.find("p", {"class":"link color-dark"}).text
    cant = categoria.find("p", {"class":"link--sm color-gray-1"}).text
    precio = categoria.find("div", {"class":"title-md color-primary-1"}).text

    #obtener la url de la imagen en el html
    url_img = categoria.find("img")['data-src']#o la src
    #peticion de la imagen al servidor
    r = request.get(url_img)
    # almacenando imagen en bytes y en memoria ram
    file = io.BytesID(r.content)
    #abriendo la imagen en bits desde memoria
    img = Image.open(file)
    #guardando la imagen en la ruta definida y con el formato requerido
    img.save(path_photos + "\\" + str(id) + ".jpg")
    i += 1
    print(f"marca : {marca}, id : {id}, cantidad: {cant}, precio : {precio}, imagen : {i})

win32api.MessageBox(false,'proceso terminado', 'finalizado', 0x00001000)
