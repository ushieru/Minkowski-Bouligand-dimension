import cv2
import math
import uuid
from minkowski_bouligand_dimension import MinkowskiBouligandDimension

if __name__ == "__main__":
    img = cv2.imread("resources/mexico.png")
    exponente = 100
    resultados = []
    minkowskiBouligandDimension = MinkowskiBouligandDimension(img)
    height, width, _ = img.shape

    for i in range(24):
        u = uuid.uuid1()
        _, newImage = minkowskiBouligandDimension.getData(exponente, height, width)
        cv2.imwrite('out/mexico%s.png' % (u), newImage)
        exponente += 20