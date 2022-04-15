#paso 1: pip install selenium
#paso 2: pip install pandas
#paso 3: descargar el driver segun el navegador

from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('webdriver\\chromedriver')

#leer data frame en formato csv con pandas
dataframe = pd.read_cvs('archivo.csv', encoding = 'latin-1')

#ciclo for para ejecutar accion por cada row del dataframe

#una buena practica seria encerrar el for en un try y catch para
# que se ejecuten las acciones antes de cargar toda la pagina.

for data in dataframe:
    #abrir formulario
    driver.get('https://form.cl') #ruta de formulario 

    #asignar datos de cada row a una variable
    index = data['ID']
    nombre = data['NOMBRES']
    correo = data['EMAIL']
    sexo = data['SEXO']
    rubro = data['RUBRO']

    #identificar los campos para ingresar la row al form, en este caso con xpath
    driver.find_element_by_xpath('xpath del input')

    #enviar datos a un input text
    driver.find_element_by_xpath('').send_keys(index)
    #enviar datos a un input radio button
    sexoOptions = {
        'mujer': 'xpath de mujer',
        'hombre':'xpath de hombre',
        'otro':'xpath de otro'
    }
    driver.find_element_by_xpath('').click(sexoOptions[sexo])
    #enviar datos a un input select
    rubroOptions =  {
        'mujer': 'xpath de salud',
        'hombre':'xpath de ',
        'otro':'xpath de otro'
    }#muchas veces los options pueden tener demasiadas opciones, en este caso mejor hacer un 
    #scrapping previo para obtener todos los elementos.
    driver.find_element_by_xpath('').click(rubroOptions[rubro]) 

    #antes de enviar puedo poner un time, para que la pagina cargue todo bien
    time.sleep(3)

    #enviar datos 
    driver.find_element_by_xpath('boton enviar xpath').click

    #si el form tiene un boton atras, o limpiar campos , se puede incluir el click en 
    #vez de volver a cargar el form al inicio del for.