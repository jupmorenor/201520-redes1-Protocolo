# -*- coding:utf-8 -*-
'''
Created on 22/11/2015
@author: Juan Pablo Moreno - 20111020059
'''
import socket

class Transmisor(object):
	'''
	Clase que implementa la conexion, transmision y recepcion de mensajes
	mediante la encapsulacion de un socket
	'''

	def __init__(self):
		self.conector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def conectar_servidor(self, port):
		self.conector.bind((socket.gethostname(), port))
	
	def conectar_cliente(self, host):
		self.conector.connect(host)
		
	def enviar(self, mensaje):
		pass
	
	def recibir(self):
		mensaje = ''
		return mensaje