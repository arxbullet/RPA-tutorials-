#INSTALAR TERESACT : https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWtaQ2diUjlLSTdZZmtJYVlYVC1KUUQ3WkE2QXxBQ3Jtc0tsZS1BaDJvYW1iSWtJRE5SSTdKajNpOFlZMi1mNldRSl9hcXRzOWpWeWFHNVoyaGdTeGJoVjllZGVrUmVFSXU0MVhuOHNIaVFMY2IxRUpiak5WdTNZcTFVLXBSb1M5bFRmSllpXzNCaTlIYUxQLUxSaw&q=https%3A%2F%2Fgithub.com%2FUB-Mannheim%2Ftesseract%2Fwikihttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWtaQ2diUjlLSTdZZmtJYVlYVC1KUUQ3WkE2QXxBQ3Jtc0tsZS1BaDJvYW1iSWtJRE5SSTdKajNpOFlZMi1mNldRSl9hcXRzOWpWeWFHNVoyaGdTeGJoVjllZGVrUmVFSXU0MVhuOHNIaVFMY2IxRUpiak5WdTNZcTFVLXBSb1M5bFRmSllpXzNCaTlIYUxQLUxSaw&q=https%3A%2F%2Fgithub.com%2FUB-Mannheim%2Ftesseract%2Fwiki
#CONFIGURAR VARIABLES DE ENTORNO : editamos la variable path y agregamos donde instalamos el teseract 
#instalar libreria pytesseract 

import pytesseract as tsc 
import time
import os 

ruta = r"ruta imagen"  #agregamos la r para indicar que es una ruta
lista = os.listdir(ruta) #para que acceda a la ruta de las imagenes si estas estan en el sistema

for elemento in lista : 
    if elemento.split('.')[-1] in ('png', 'jpg'):
        text = tsc.image_to_string(ruta + "\\" + elemento, config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890') #el param de configuracion ayuda a 
        #hacer mas exacta la presicion.

#tesseract detecta el codigo mas resaltante, y no los detalles, asi que se puede
#mejorar la imagen para resolver estas cosas.