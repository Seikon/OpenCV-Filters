import cv2
import sys
import frameBlackWhiteFilter
import random as random

#Pedimos ruta fichero video
ruta_video = input("Ruta completa del fichero: ")
	
cap = cv2.VideoCapture(ruta_video)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fps = cap.get(cv2.CAP_PROP_FPS)

#Define los objetos necesarios para la escritura de video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc, fps, (frame_width,frame_height), True)

numero_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
numero_frames_procesados = 0

contador = 0
colorFondo = frameBlackWhiteFilter.Color.NEGRO

while(cap.isOpened()):

	#Generamos el color en cada frame
	if contador > 45:
		if colorFondo == frameBlackWhiteFilter.Color.NEGRO:
			colorFondo = frameBlackWhiteFilter.Color.BLANCO
		elif colorFondo == frameBlackWhiteFilter.Color.BLANCO:
			colorFondo = frameBlackWhiteFilter.Color.NEGRO
		contador = 0
		
		
	#Calculamos el porcentaje con los frames ya procesados y el total de frames
	porcentaje = (numero_frames_procesados / numero_frames) * 100
	#Mostramos el porcentaje
	print('{0:.3g}'.format(porcentaje), "%", numero_frames_procesados , "frames procesados de ",numero_frames)
	#Leemos cada frame
	ret,frame = cap.read()
	if ret == False:
		break
	#Aplicamos el filtro
	blackWhite = frameBlackWhiteFilter.frameBlackWhiteFast(frame, colorFondo);
	#Escribe en el buffer de video
	out.write(blackWhite)
	numero_frames_procesados += 1
	contador +=1
	
print('Proceso Finalizado')
cap.release()
out.release
cv2.destroyAllWindows()





