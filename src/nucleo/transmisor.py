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
		self._conector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket = None
		self._dir = ""
		self.tamMensaje = 0
	
	def crear_servidor(self, port):
		nombre = socket.gethostname()
		self._conector.bind((nombre, port))
		self._conector.listen(5)
		return nombre
		
	def conectar_servidor(self):
		self._socket, self._dir = self._conector.accept()
		return True
	
	def conectar_cliente(self, host):
		self._conector.connect(host)
		
	def enviar(self, mensaje):
		if self._socket is None:
			self._conector.send(mensaje)
		else:
			self._socket.send(mensaje)
	
	def recibir(self):
		mensaje = ""
		if self._socket is None:
			mensaje += self._conector.recv(32)
		else:
			mensaje = self._socket.recv(32)
		return mensaje
	
	def terminar(self):
		self._conector.close()

