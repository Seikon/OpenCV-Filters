import numpy as np
import random as random
import matplotlib.pyplot as plt
import cv2
import cython
from enum import Enum

class Color(Enum):
		NEGRO = 1
		BLANCO = 2

	
def frameBlackWhiteFast(imagen, color):

	fondo = cv2.imread("C:/Users/Alex/Desktop/bboy videos/croma.jpg")

	blur = cv2.GaussianBlur(imagen,(7,7),0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	#Crea las mascaras
	mascara_color = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
	#Si el fondo es negro, invierte la mascara			
	if color == Color.NEGRO:
		mascara_color = cv2.bitwise_not(mascara_color)
		
	blackWhite = cv2.cvtColor(mascara_color, cv2.COLOR_GRAY2RGB)
	
	return blackWhite
