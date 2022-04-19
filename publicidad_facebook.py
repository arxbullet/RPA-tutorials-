#bot de automatizacion de publicidad de facebook
#pasos
"""
1. abrir navegador
2. ir a facebook.com
3. autenticarse ?
4. cliclear grupos
4. recorrer grupos y publicar en todos 
4. tener la opcion de publicar solo en los que cumplan cierto criterio.
5. buscar crear publicación
6. revisar carpeta con txt e imagenes
7. llenar form publicación
8. enviar
9. avisar ? console.log o mail 
10. examinar bach para automatizar.
11. hacer un archivo requirements.txt
"""

# 1 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time


driver = webdriver.Chrome('.\\chromedriver')
driver.maximize_window()

# 2
url = 'https://www.facebook.com/'
driver.get(url)

# 3
credenciales = r'.\\credenciales.txt'
df = pd.read_csv(credenciales,sep=",")
usuario = str(df['usuario'][0])
contraseña = str(df['contraseña'][0])

input_correo = '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input'
input_contraseña = '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input'
boton_login = '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'

driver.find_element_by_xpath(input_correo).send_keys(usuario)
time.sleep(1)
driver.find_element_by_xpath(input_contraseña).send_keys(contraseña)
time.sleep(1)
driver.find_element_by_xpath(boton_login).click()

#4 
boton_grupos = '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a'
driver.find_element_by_xpath(boton_grupos).click()
time.sleep(2)
#5
grupos = driver.find_elements_by_class_name("iqfcb0g7 tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p")
print(grupos)

# 6 
boton_vender = '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div'
#driver.find_element_by_xpath(boton_vender).click()
boton_Articulo = '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/span/div/div'
#driver.find_element_by_xpath(boton_Articulo).click()

# hacer dataframe de la publicacion 

"""estados =  {
        'nuevo': 'xpath de salud',
        'usadocomonuevo':'xpath de ',
        'usadobuenestado':'xpath de otro',
        'usadoaceptable':'xpath de otro'
    }

imagen = '//*[@id="mount_0_0_Pc"]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div'
titulo = '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/label/div/div/input'
precio  = '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[3]/div/div/label/div/div/input'
descripcion ='/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[5]/div/div/label/div/div/textarea'
estado  = '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[4]/div/div/div/label'
etiquetas = '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[6]/div/div/div/label/div/div/div/div[2]/textarea'
enviar = '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[9]/div'

driver.find_element_by_xpath(imagen).send_keys('')
driver.find_element_by_xpath(precio).send_keys('')
driver.find_element_by_xpath(descripcion).send_keys('')
driver.find_element_by_xpath(estado).send_keys('')
driver.find_element_by_xpath(etiquetas).send_keys('')
driver.find_element_by_xpath(enviar).click()"""
