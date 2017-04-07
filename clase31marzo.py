import random
import pygame,sys
from pygame.locals import *

ANCHO = 600
ALTO= 600
BLANCO = (255,255,255)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
NEGRO = (0,0,0)

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])



	plantilla = pygame.image.load('pajaritos.png').convert_alpha()
	lista=[]
	cr_an=125
	cr_al=83
	#este for carga los sprites d elos pajaros (4 imagenes )
	for i in range(4):
		cuadro=plantilla.subsurface(0+(i*cr_an),0,cr_an,cr_al) #125 en x, 83 en y
		lista.append(cuadro)#a;adiendo imagenes en la lista
		

	fin = False
	reloj = pygame.time.Clock()
	i=0
	while not fin:
		#ZONA DE EVENTOS 
		for event in pygame.event.get():		
			if event.type == pygame.QUIT:
				fin = True

		#esto pone la animaciones de las 4 imagenes de los pajaros en una misma posicion
		pantalla.blit(lista[i],[100,100])
		i+=1
		if i ==4:
			i=0
		pygame.display.flip()
		reloj.tick(40)