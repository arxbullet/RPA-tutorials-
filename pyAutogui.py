#instalar pyautogui para usar robot de posiciones
import pyautogui as robot
import time

#ingresar a chrome desde el escritorio
""" abrir cmd, llamar a pyrhon, importar pyautogui, y escribir pyautogui.displaymouseposition, para 
obtener las posiciones en la pantalla del icono de chrome en el escritorio"""

chrome = -1606, 854
buscador =  916,  65
invitado =   116 , 770
buscar = 499, 49
cancion = 670, 129
exit = 1510, 17

#metodo para hacer click 

time.sleep(5)

def abrir(x, click=1):
    robot.moveTo(x)
    robot.click(clicks=click)

#abrir google

abrir(chrome, click=2)
time.sleep(2)

#maximizar pantalla 
robot.hotkey("alt","space")
time.sleep(0.5)
robot.typewrite("x")
time.sleep(4)

#ingresar a youtube
abrir(invitado)
abrir(buscador)
robot.typewrite('www.youtube.com')
robot.hotkey('enter')
time.sleep(5)

#buscar cancion
listaCanciones = ['never gonna give u up', 'take on me']

for elemento in range(len(listaCanciones)):
    abrir(buscar, click='3')
    robot.typewrite(listaCanciones[elemento])
    robot.hotkey('enter')
    time.sleep(2)
    abrir(cancion)
    time.sleep(5)

abrir(exit)
print('proceso terminado')

#seleccionar cancion
#disfrutar cancion por un tiempo
#pasar a la siguiente cancion
