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
	PPT			Solicitud para transmision
	LPR			Listo para recibir informacion de datos o de control
	CTR			Identifica una trama donde lo que se va a transmitir es informacion de control
	DAT			Identifica una trama donde lo que se va a transmitir es informacion de datos
	NUM			Numero de la trama que se esta enviando
	INFORMACION	Campo de tamaño variable donde se pone la informacion
	'''

	def __init__(self):
		self.INDICADOR=10000001
		self.ACK=0
		self.ENQ=0
		self.CTR=0
		self.DAT=0
		self.PPT=0
		self.LPT=0
		self.NUM=0
		self.INFO=''
		
	def __call__(self):
		return str(self.INDICADOR)+str(self.ACK)+str(self.ENQ)+str(self.CTR)+str(self.DAT)+str(self.PPT)+\
	str(self.LPT)+str(self.NUM)+self.INFO+str(self.INDICADOR)
		
if __name__ =='__main__':
	print Trama()()	