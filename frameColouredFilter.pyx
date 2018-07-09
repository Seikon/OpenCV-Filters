import numpy as np
import random as random
import matplotlib.pyplot as plt
import cv2
import cython
	
def frameColouredFilterFast(imagen, color):
	cdef int x = 0
	cdef int y = 0
	cdef int ancho = imagen.shape[1]
	cdef int alto = imagen.shape[0]
	cdef double b
	cdef double g
	cdef double r
	cdef double h
	cdef double s
	cdef double v
	bajo_verde = 90
	alto_verde = 125

	#Se obtiene el alto y el ancho de la imagen

	#Recorre la imagen alto x ancho
	for y in xrange(alto):
		for x in xrange(ancho):
			
			b = imagen[y, x, 0]
			g = imagen[y, x, 1]
			r = imagen[y, x, 2]
			
			h, s, v = rgb2hsv(r,g,b)
			#Si h se encuentra en el rango de verdes, se vuelve negro
			if(h >= bajo_verde) and (h <= alto_verde):
				imagen[y,x] = [0,0,0]
			else:
				imagen[y,x] = color
				
	return imagen
	
def rgb2hsv(r, g, b):
	r, g, b = r/255.0, g/255.0, b/255.0
	mx = max(r, g, b)
	mn = min(r, g, b)
	df = mx-mn
	if mx == mn:
		h = 0
	elif mx == r:
		h = (60 * ((g-b)/df) + 360) % 360
	elif mx == g:
		h = (60 * ((b-r)/df) + 120) % 360
	elif mx == b:
		h = (60 * ((r-g)/df) + 240) % 360
	if mx == 0:
		s = 0
	else:
		s = df/mx
	v = mx
	return h, s, v