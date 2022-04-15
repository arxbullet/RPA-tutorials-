#paso 1: pip install selenium
#paso 2: pip install pandas
#paso 3: descargar el driver segun el navegador

from selenium import webdriver #chrome driver debe estar a la misma version que nuestro chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time

driver = webdriver.Chrome('webdriver\\chromedriver')

#maximizar pantalla 
driver.maximize_window()

#abrir pagina web
driver.get('url')

#leer data de excel
excel = r'ruta_Excel'
df = pd.read_excel(excel)
user = df['usuario'][0]
passwd = df['password'][0]

#selectores 
boton_iniciar_Sesion = 'valor copy selector'
input_usuario = 'valor copy selector'
input_contraseña = 'valor copy selector'
boton_login = 'valor copy selector'

#ACCIONES 

driver.find_element_by_css_selector(boton_iniciar_Sesion).click()
driver.find_element_by_css_selector(input_usuario).send_keys(user)
driver.find_element_by_css_selector(input_contraseña).send_keys(passwd)
driver.find_element_by_css_selector(boton_login).click()

#MAS ACCIONES DENTRO DE LA PAGINA -->

time.sleep(7)

driver.quit()
