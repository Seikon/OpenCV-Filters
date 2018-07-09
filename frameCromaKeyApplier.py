import cv2
import sys
import frameCromaKey
import random as random

#Pedimos ruta fichero video
ruta_video = input("Ruta completa del fichero: ")

#Pedimos el color del croma
print("Seleccione color del croma")
print("1 - Rojo")
print("2 - Verde")
print("3 - Azul")
color_croma = int(float(input("")))

while color_croma < 1 or color_croma > 3:
	print("Seleccione color del croma")
	print("1 - Rojo")
	print("2 - Verde")
	print("3 - Azul")
	color_croma = int(float(input("")))
	
if color_croma == 1:
	color_croma = frameCromaKey.Color.ROJO	
elif color_croma == 2:
	color_croma = frameCromaKey.Color.VERDE	
elif color_croma == 3:
	color_croma = frameCromaKey.Color.AZUL		


cap = cv2.VideoCapture(ruta_video)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fps = cap.get(cv2.CAP_PROP_FPS)

#Define los objetos necesarios para la escritura de video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc, fps, (frame_width,frame_height), True)

numero_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
numero_frames_procesados = 0

while(cap.isOpened()):
		
	#Calculamos el porcentaje con los frames ya procesados y el total de frames
	porcentaje = (numero_frames_procesados / numero_frames) * 100
	#Mostramos el porcentaje
	print('{0:.3g}'.format(porcentaje), "%", numero_frames_procesados , "frames procesados de ",numero_frames)
	#Leemos cada frame
	ret,frame = cap.read()
	if ret == False:
		break
	#Aplicamos el filtro
	cromaFilter = frameCromaKey.frameCromaKeyFast(frame, color_croma);
	#Escribe en el buffer de video
	out.write(cromaFilter)
	numero_frames_procesados += 1
	
print('Proceso Finalizado')
cap.release()
out.release
cv2.destroyAllWindows()





