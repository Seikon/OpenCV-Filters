import numpy as np
import random as random
import matplotlib.pyplot as plt
import cv2
import cython
from enum import Enum

class Color(Enum):
		ROJO = 1
		VERDE = 2
		AZUL = 3

	
def frameCromaKeyFast(imagen, color):

	fondo = cv2.imread("C:/Users/Alex/Desktop/bboy videos/croma.jpg")

	blur = cv2.GaussianBlur(imagen,(7,7),0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	#Rango de colores de verdes
	#Crea las mascaras
	if color == Color.VERDE:
		mascara_color = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
	elif color == Color.AZUL:
		mascara_color = cv2.inRange(hsv, (100,0,0), (140,255,255))
	
	mascara_invertida = cv2.bitwise_not(mascara_color)
	
	mascara_insertada = cv2.bitwise_and(imagen,imagen, mask= mascara_invertida)
	
	mascara_fondo = cv2.bitwise_and(fondo,fondo, mask= mascara_color)
	
	croma_key = cv2.add(mascara_fondo, mascara_insertada)
	
	return croma_key
