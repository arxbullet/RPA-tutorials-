
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
df = pd.read_excel(excel, sheet_name='lista canciones')

#Copy full xpath es mucho mas preciso que las clases y los selectores

busqueda_youtube = 'fullxpath'
boton_buscar = 'fullxpath'
path_cancion = 'fullxpath'

# for para canciones

for i in df.index:
    cancion = df['cancion'][i]
    driver.find_element_by_xpath(busqueda_youtube).send_keys(cancion)
    driver.find_element_by_xpath(boton_buscar).click()

    #esperar a que aparescan las canciones (asincronicidad)
    
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_all_elements_located(By.XPATH, path_cancion))

    driver.find_element_by_xpath(path_cancion).click

    time.sleep(5)

    #borrar busqueda anterior

    driver.find_element_by_xpath(busqueda_youtube).clear()

driver.quit()
