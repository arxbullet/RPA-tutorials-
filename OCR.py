import cv2
import easyocr

reader = easyocr.Reader(["es"])

image = cv2.imread("imagen.png")

result = reader.readtext(image)

for res in result:
    print("result:",res)

cv2.imshow("Image", image)

cv2.waitkey(0)

cv2.destroyAllWindows()
