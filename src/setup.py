'''
Created on 22/11/2015
@author: Juan Pablo Moreno - 20111020059
'''
import sys
from PyQt4.QtGui import QApplication
from GUI import Ventana

def main():
	app = QApplication(sys.argv)
	v = Ventana()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()