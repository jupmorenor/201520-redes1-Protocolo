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

	def __init__(self, host):
		self.conector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conector.bind(host)
		