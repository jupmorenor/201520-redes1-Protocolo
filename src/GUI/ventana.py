'''
Created on 22/11/2015
@author: Juan Pablo Moreno - 20111020059
'''
from PyQt4.QtGui import QMainWindow

class Ventana(QMainWindow):
	'''
	Ventana de interfaz grafica para la aplicacion
	'''

	def __init__(self):
		super(Ventana, self).__init__()
		self.show()