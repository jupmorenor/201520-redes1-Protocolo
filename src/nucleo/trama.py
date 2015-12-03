# -*- coding:utf-8 -*-
'''
Created on 22/11/2015
@author: Juan Pablo Moreno - 20111020059
'''

class Trama(object):
	'''
	Clase que encapsula una trama o frame
	INDICADOR	Indicador, marca el inicio y el final de una trama
	ACK			Reconocimiento de llegada de la informacion
	ENQ			Ultima trama a ser enviada
	CTR			Identifica una trama donde lo que se va a transmitir es informacion de control
	DAT			Identifica una trama donde lo que se va a transmitir es informacion de datos
	PPT			Solicitud para transmision
	LPR			Listo para recibir informacion de datos o de control
	NUM			Numero de la trama que se esta enviando
	INFORMACION	Campo de tamaño variable donde se pone la informacion
	'''

	def __init__(self):
		self.INDICADOR="10000001"
		self.ACK="0"
		self.ENQ="0"
		self.CTR="0"
		self.DAT="0"
		self.PPT="0"
		self.LPR="0"
		self.NUM="0"
		self.INFO=""
		
	def esACK(self):
		return self.ACK=="1"
	
	def esENQ(self):
		return self.ENQ=="1"
	
	def esPPT(self):
		return self.PPT=="1"
	
	def esLPR(self):
		return self.LPR=="1"
	
	def esDAT(self):
		return (self.DAT=="1" and self.ENQ=="0")
		
	def __call__(self):
		return self.INDICADOR+self.ACK+self.ENQ+self.CTR+self.DAT+self.PPT+\
	self.LPR+self.NUM+self.INFO+self.INDICADOR
		
if __name__ =='__main__':
	print Trama()()	