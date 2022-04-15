# install cv2
import cv2
import os

path_photos = 'C:\Users\DUOC\Imágenes'

lista = os.listdir(path_photos)

for i in lista :
    img = cv2.imread(path_photos+"\\"+i)
    valor = 2
    width = int(img.shape[1]*valor)
    height = int(img.shape[0]*valor)
    dim = (width, height)
    resized = cv2.resized(img, dim)
    cv2.imwrite(path_photos+"\\"+i, resized)