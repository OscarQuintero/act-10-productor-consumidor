# -*- coding: utf_8 -*-
import random
import time
from collections import deque
import threading 
import os
from pynput import keyboard

RETARDO = 2
semaforoGeneral = -1 
semaforoTurno = 0 


def wait(semaforo):
	semaforo -= 1
	return semaforo

def signal(semaforo):
	semaforo += 1
	return semaforo

def rellenarConCeros(n):
	s = ''
	if n < 10:
		s = '0'	
	s += str(n)
	return s
	
def limpiarPantalla():	
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "ct" or os.name == "nt" or os.name == "dos"):
		os.system("cls")
	
def pulsa(k):
	# print('Se ha pulsado la tecla ' + str(k))
	pass
def suelta(k):
	# print('Se ha soltado la tecla ' + str(k))
	if k == keyboard.Key.esc:
		exit()
	pass

class Productor:
	"""docstring for ClassName"""
	def __init__(self):
		pass
		
class Consumidor:
	def __init__(self):
		pass

class Contenedor:
	"""docstring for ClassName"""
	def __init__(self, size):
		self.capacidad = size
		self.productos = 0
		self.buffer = []
		self.indiceEntrada = 0
		self.indiceSalida = 0
		for k in range(size):
			self.buffer.append("_")
		

	def agregar(self):
		print("Agregando","productos")
		self.productos += 1
		self.buffer[self.indiceEntrada] = '*'
		self.indiceEntrada += 1
		self.indiceEntrada = self.indiceEntrada % self.capacidad
		return

	def consumir(self):
		print("Consumiendo","productos")
		self.productos -= 1
		self.buffer[self.indiceSalida] = '_'
		self.indiceSalida += 1
		self.indiceSalida = self.indiceSalida % self.capacidad
		return
	def imprimir(self):
		print("Contenedor con", self.productos, "de", self.capacidad, ":")
		auxStr = '|'
		labelStr = ''
		for i in range(self.capacidad):
			auxStr += self.buffer[i] + ' |'
		print(auxStr)
		for k in range(self.capacidad):
			labelStr += ' ' + rellenarConCeros(k+1)
		print(labelStr)
		return

# def f():
# 	c = 0
# 	while c < 100:
		
# 		print(threading.current_thread().getName())
# 		c += 1

# hilo1 = threading.Thread(target=f)
# hilo2 = threading.Thread(target=f)


#####################################################################

limpiarPantalla()
print("Actividad 11 - Oscar Alejandro Quintero Iñiguez")
print("Seminario de Sistemas Operativos - 2021 B")
print("\n")
print("Creando contenedor...")
print("\n")

contenedor = Contenedor(22)

print("Contenedor vacio:")
print("\n")

contenedor.imprimir()
print("Iniciando proceso aleatorio de designación de turnos")
time.sleep(3)

escuchador = keyboard.Listener(pulsa, suelta)
escuchador.start()
#Se elige al azar el turno del consumidor o del productor
#El consumidor es 1 y el productor 2
CONSUMIDOR = 1
PRODUCTOR = 2

while escuchador.is_alive():
	
	limpiarPantalla()
	turno = random.randint(1,2)

	if(turno == CONSUMIDOR):
		print("\n")
		print("--------------------")
		print("Turno del Consumidor")
		print("--------------------")
		print("semáforo general:",semaforoGeneral, "\t", "semáforo turno:", semaforoTurno)
		print("\n")
		print("Consumidor quiere entrar al contenedor")

		if semaforoTurno < 0:
			print("--->Intento denegado por contenedor BLOQUEADO")
		else:
			
			print("--->Intento permitido")
			semaforoTurno = wait(semaforoTurno)
			print("\n")
			print("Intentando consumir un producto")
			if semaforoGeneral < 0:
				print("------->Intento denegado por contenedor BLOQUEADO\n")
			else:
				print("------->Intento permitido")	
				contenedor.consumir()
				semaforoGeneral = wait(semaforoGeneral)
			semaforoTurno = signal(semaforoTurno)
		
	

	if(turno == PRODUCTOR):
		print("\n")
		print("--------------------")
		print("Turno del Productor")
		print("--------------------")
		print("semáforo general:",semaforoGeneral, "\t", "semáforo turno:", semaforoTurno)
		print("\n")
		print("Productor quiere entrar al contenedor")

		if semaforoTurno < 0:
			print("--->Intento denegado por contenedor BLOQUEADO")
		else:
			
			print("--->Intento permitido")
			semaforoTurno = wait(semaforoTurno)
			print("\n")
			print("Intentando añadir un producto")
			if semaforoGeneral > 22:
				print("------->Intento denegado por contenedor BLOQUEADO\n")
			else:
				print("------->Intento permitido")	
				contenedor.agregar()
				semaforoGeneral = signal(semaforoGeneral)
			semaforoTurno = signal(semaforoTurno)
	
	print("\n")	
	contenedor.imprimir()
	time.sleep(RETARDO)	





