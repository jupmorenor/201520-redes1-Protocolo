'''
Created on 22/11/2015
@author: Juan Pablo Moreno - 20111020059
'''
from PyQt4.QtGui import QWidget, QFrame, QSplitter, QHBoxLayout, QVBoxLayout, QLabel
from PyQt4.QtGui import QLineEdit, QCheckBox, QPushButton, QInputDialog, QMessageBox
from PyQt4.QtCore import Qt
from nucleo import Trama, Transmisor


class Ventana(QWidget):
	'''
	Ventana de interfaz grafica para la aplicacion
	'''

	def __init__(self):
		super(Ventana, self).__init__()
		
		self._CLIENTE = "Cliente"
		self._SERVIDOR = "Servidor"
		
		self.rol = ""
		self.pasos = []
		self.mensaje = []
		
		self.labelSemanticaT = QLabel("Semantica: ")
		self.labelSemanticaR = QLabel("Semantica: ")
		self.labelSemanticaT.adjustSize()
		self.labelSemanticaR.adjustSize()
		
		#campos de texto transmisor
		self.textoMensajeT = QLineEdit()
		self.textoFramesT = QLineEdit("1")
		self.textoIndicador1T = QLineEdit()
		self.textoACKT = QLineEdit()
		self.textoENQT = QLineEdit()
		self.textoCTRT = QLineEdit()
		self.textoDATT = QLineEdit()
		self.textoPPTT = QLineEdit()
		self.textoLPRT = QLineEdit()
		self.textoNUMT = QLineEdit()
		self.textoInfoT = QLineEdit()
		self.textoIndicador2T = QLineEdit()
		
		#Selectores de campos de control
		self.checkACK = QCheckBox()
		self.checkENQ = QCheckBox()
		self.checkCTR = QCheckBox()
		self.checkDAT = QCheckBox()
		self.checkPPT = QCheckBox()
		self.checkLPR = QCheckBox()
		
		#boton de transmision
		self.botonTransmisor = QPushButton("ENVIAR")
		
		#campos de texto receptor
		self.textoIndicador1R = QLineEdit()
		self.textoACKR = QLineEdit()
		self.textoENQR = QLineEdit()
		self.textoCTRR = QLineEdit()
		self.textoDATR = QLineEdit()
		self.textoPPTR = QLineEdit()
		self.textoLPRR = QLineEdit()
		self.textoNUMR = QLineEdit()
		self.textoInfoR = QLineEdit()
		self.textoIndicador2R = QLineEdit()
		self.textoMensajeR = QLineEdit()
			
		#boton de respuesta
		self.botonRecibir = QPushButton("RECIBIR")
		self.trama = Trama()
		self.trama_anterior = None
		self.transmisor = Transmisor()
		self._inicializar()
				
	def _inicializar(self):
		self.setWindowTitle("Protocolo de transmision de datos")
		
		#------------------------------------#
		#		ELEMENTOS DEL TRANSMISOR	 #
		#------------------------------------#
		
		#Etiquetas transmisor
		tituloT = QLabel("TRANSMISION")
		labelMensajeT = QLabel("Mensaje a transmitir:")
		labelFramesT = QLabel("Numero de frames:")
		labelIndicador1T = QLabel("INDICADOR")
		labelACKT = QLabel("ACK")
		labelENQT = QLabel("ENQ")
		labelCTRT = QLabel("CTR")
		labelDATT = QLabel("DAT")
		labelPPTT = QLabel("PPT")
		labelLPRT = QLabel("LPR")
		labelNUMT = QLabel("NUM")
		labelInfoT = QLabel("INFORMACION")
		labelIndicador2T = QLabel("INDICADOR")
				
		tituloT.adjustSize()
		labelMensajeT.adjustSize()
		labelFramesT.adjustSize()
		labelIndicador1T.adjustSize()
		labelACKT.adjustSize()
		labelENQT.adjustSize()
		labelCTRT.adjustSize()
		labelDATT.adjustSize()
		labelPPTT.adjustSize()
		labelLPRT.adjustSize()
		labelNUMT.adjustSize()
		labelInfoT.adjustSize()
		labelIndicador2T.adjustSize()
			
		#agregar los elementos al segundo nivel de layout
		fila1 = QHBoxLayout()
		fila2 = QHBoxLayout()
		fila3 = QHBoxLayout()
		fila4 = QHBoxLayout()
		cajaTransmisor = QVBoxLayout()
		
		fila1.addWidget(tituloT)
		fila2.addWidget(labelMensajeT)
		fila2.addWidget(self.textoMensajeT)
		fila2.addWidget(labelFramesT)
		fila2.addWidget(self.textoFramesT)
		fila4.addWidget(self.labelSemanticaT)
		
		fila3_1 = QVBoxLayout()
		fila3_2 = QVBoxLayout()
		fila3_3 = QVBoxLayout()
		fila3_4 = QVBoxLayout()
		fila3_5 = QVBoxLayout()
		fila3_6 = QVBoxLayout()
		fila3_7 = QVBoxLayout()
		fila3_8 = QVBoxLayout()
		fila3_9 = QVBoxLayout()
		fila3_10 = QVBoxLayout()
		
		fila3_1.addWidget(labelIndicador1T)
		fila3_1.addWidget(self.textoIndicador1T)
		fila3_1.setAlignment(Qt.AlignTop)
		fila3_2.addWidget(labelACKT)
		fila3_2.addWidget(self.textoACKT)
		fila3_2.addWidget(self.checkACK)
		fila3_3.addWidget(labelENQT)
		fila3_3.addWidget(self.textoENQT)
		fila3_3.addWidget(self.checkENQ)
		fila3_4.addWidget(labelCTRT)
		fila3_4.addWidget(self.textoCTRT)
		fila3_4.addWidget(self.checkCTR)
		fila3_5.addWidget(labelDATT)
		fila3_5.addWidget(self.textoDATT)
		fila3_5.addWidget(self.checkDAT)
		fila3_6.addWidget(labelPPTT)
		fila3_6.addWidget(self.textoPPTT)
		fila3_6.addWidget(self.checkPPT)
		fila3_7.addWidget(labelLPRT)
		fila3_7.addWidget(self.textoLPRT)
		fila3_7.addWidget(self.checkLPR)
		fila3_8.addWidget(labelNUMT)
		fila3_8.addWidget(self.textoNUMT)
		fila3_8.setAlignment(Qt.AlignTop)
		fila3_9.addWidget(labelInfoT)
		fila3_9.addWidget(self.textoInfoT)
		fila3_9.setAlignment(Qt.AlignTop)
		fila3_10.addWidget(labelIndicador2T)
		fila3_10.addWidget(self.textoIndicador2T)
		fila3_10.setAlignment(Qt.AlignTop)
		fila3.addLayout(fila3_1)
		fila3.addLayout(fila3_2)
		fila3.addLayout(fila3_3)
		fila3.addLayout(fila3_4)
		fila3.addLayout(fila3_5)
		fila3.addLayout(fila3_6)
		fila3.addLayout(fila3_7)
		fila3.addLayout(fila3_8)
		fila3.addLayout(fila3_9)
		fila3.addLayout(fila3_10)
		fila3.addWidget(self.botonTransmisor)
		
		cajaTransmisor.addLayout(fila1)
		cajaTransmisor.addLayout(fila2)
		cajaTransmisor.addLayout(fila3)
		cajaTransmisor.addLayout(fila4)
		
		#------------------------------------#
		#		ELEMENTOS DEL RECEPTOR		 #
		#------------------------------------#
		
		#Etiquetas receptor
		tituloR = QLabel("RECEPCION")
		labelFrameR = QLabel("Trama recibida:")
		labelRespuestaR = QLabel("Recibido: ")
		labelIndicador1R = QLabel("INDICADOR")
		labelACKR = QLabel("ACK")
		labelENQR = QLabel("ENQ")
		labelCTRR = QLabel("CTR")
		labelDATR = QLabel("DAT")
		labelPPTR = QLabel("PPT")
		labelLPRR = QLabel("LPR")
		labelNUMR = QLabel("NUM")
		labelInfoR = QLabel("INFORMACION")
		labelIndicador2R = QLabel("INDICADOR")
		labelMensajeR = QLabel("Mensaje recibido:")
		
		tituloR.adjustSize()
		labelFrameR.adjustSize()
		labelRespuestaR.adjustSize()
		labelIndicador1R.adjustSize()
		labelACKR.adjustSize()
		labelENQR.adjustSize()
		labelCTRR.adjustSize()
		labelDATR.adjustSize()
		labelPPTR.adjustSize()
		labelLPRR.adjustSize()
		labelNUMR.adjustSize()
		labelInfoR.adjustSize()
		labelIndicador2R.adjustSize()
		labelMensajeR.adjustSize()
				
		#agregar los elementos al segundo nivel de layout
		fila5 = QHBoxLayout()
		fila6 = QHBoxLayout()
		fila8 = QHBoxLayout()
		fila9 = QHBoxLayout()
		fila10 = QHBoxLayout()
		fila11 = QHBoxLayout()
		cajaReceptor = QVBoxLayout()
				
		fila5.addWidget(tituloR)
		fila6.addWidget(labelFrameR)
		fila8.addWidget(labelRespuestaR)
		
		#fila9
		fila9_1 = QVBoxLayout()
		fila9_2 = QVBoxLayout()
		fila9_3 = QVBoxLayout()
		fila9_4 = QVBoxLayout()
		fila9_5 = QVBoxLayout()
		fila9_6 = QVBoxLayout()
		fila9_7 = QVBoxLayout()
		fila9_8 = QVBoxLayout()
		fila9_9 = QVBoxLayout()
		fila9_10 = QVBoxLayout()
		
		fila9_1.addWidget(labelIndicador1R)
		fila9_1.addWidget(self.textoIndicador1R)
		fila9_2.addWidget(labelACKR)
		fila9_2.addWidget(self.textoACKR)
		fila9_3.addWidget(labelENQR)
		fila9_3.addWidget(self.textoENQR)
		fila9_4.addWidget(labelCTRR)
		fila9_4.addWidget(self.textoCTRR)
		fila9_5.addWidget(labelDATR)
		fila9_5.addWidget(self.textoDATR)
		fila9_6.addWidget(labelPPTR)
		fila9_6.addWidget(self.textoPPTR)
		fila9_7.addWidget(labelLPRR)
		fila9_7.addWidget(self.textoLPRR)
		fila9_8.addWidget(labelNUMR)
		fila9_8.addWidget(self.textoNUMR)
		fila9_9.addWidget(labelInfoR)
		fila9_9.addWidget(self.textoInfoR)
		fila9_10.addWidget(labelIndicador2R)
		fila9_10.addWidget(self.textoIndicador2R)
		
		fila9.addLayout(fila9_1)
		fila9.addLayout(fila9_2)
		fila9.addLayout(fila9_3)
		fila9.addLayout(fila9_4)
		fila9.addLayout(fila9_5)
		fila9.addLayout(fila9_6)
		fila9.addLayout(fila9_7)
		fila9.addLayout(fila9_8)
		fila9.addLayout(fila9_9)
		fila9.addLayout(fila9_10)
		fila9.addWidget(self.botonRecibir)
		
		fila10.addWidget(self.labelSemanticaR)
		fila11.addWidget(labelMensajeR)
		fila11.addWidget(self.textoMensajeR)
		
		cajaReceptor.addLayout(fila5)
		cajaReceptor.addLayout(fila6)
		cajaReceptor.addLayout(fila8)
		cajaReceptor.addLayout(fila9)
		cajaReceptor.addLayout(fila10)
		cajaReceptor.addLayout(fila11)
		
		#------------------------------------#
				
		#agregar el segundo nivel de layout al panel
		panelTransmisor = QFrame(self)
		panelTransmisor.setFrameShape(QFrame.StyledPanel)
		panelTransmisor.setLayout(cajaTransmisor)
		
		#agregar el segundo nivel de layout al panel
		panelReceptor = QFrame(self)
		panelReceptor.setFrameShape(QFrame.StyledPanel)
		panelReceptor.setLayout(cajaReceptor)
		
		#agregar el panel al separador
		separador = QSplitter(Qt.Vertical)
		separador.addWidget(panelTransmisor)
		separador.addWidget(panelReceptor)
		
		#agregar el separador al primer layout
		caja = QVBoxLayout(self)
		caja.addWidget(separador)
		
		#agregar el layout a la ventana
		self.setLayout(caja)
		
		self.setFixedSize(800, 400)
		self._configurar()
		self.show()
		self.crear_conexion()
		
	def _configurar(self):
		
		self.textoIndicador1T.setEnabled(False)
		self.textoACKT.setEnabled(False)
		self.textoENQT.setEnabled(False)
		self.textoCTRT.setEnabled(False)
		self.textoDATT.setEnabled(False)
		self.textoPPTT.setEnabled(False)
		self.textoLPRT.setEnabled(False)
		self.textoNUMT.setEnabled(False)
		self.textoInfoT.setEnabled(False)
		self.textoIndicador2T.setEnabled(False)
		
		self.textoIndicador1R.setEnabled(False)
		self.textoACKR.setEnabled(False)
		self.textoENQR.setEnabled(False)
		self.textoCTRR.setEnabled(False)
		self.textoDATR.setEnabled(False)
		self.textoPPTR.setEnabled(False)
		self.textoLPRR.setEnabled(False)
		self.textoNUMR.setEnabled(False)
		self.textoInfoR.setEnabled(False)
		self.textoIndicador2R.setEnabled(False)
		self.textoMensajeR.setEnabled(False)
		
		self.checkACK.setEnabled(False)
		self.checkENQ.setEnabled(False)
		self.checkPPT.setEnabled(False)
		self.checkLPR.setEnabled(False)
		
		self.checkACK.stateChanged.connect(self._seleccionarACK)
		self.checkENQ.stateChanged.connect(self._seleccionarENQ)
		self.checkCTR.stateChanged.connect(self._seleccionarCTR)
		self.checkDAT.stateChanged.connect(self._seleccionarDAT)
		self.checkPPT.stateChanged.connect(self._seleccionarPPT)
		self.checkLPR.stateChanged.connect(self._seleccionarLPR)
		self.botonTransmisor.clicked.connect(self._enviar_mensaje)
		self.botonRecibir.clicked.connect(self._recibir_mensaje)
		
		self._mostrar_trama(self._SERVIDOR)
		
	def _seleccionarACK(self, estado):
		if estado == Qt.Checked:
			self.textoACKT.setText("1")
			self.checkPPT.setChecked(False)
			self.checkLPR.setChecked(False)
		else:
			self.textoACKT.setText("0")
		
	def _seleccionarENQ(self, estado):
		if estado == Qt.Checked:
			self.textoENQT.setText("1")
		else:
			self.textoENQT.setText("0")
		
	def _seleccionarCTR(self, estado):
		if estado == Qt.Checked:
			self.textoCTRT.setText("1")
			self.checkDAT.setChecked(False)
			self.checkACK.setEnabled(True)
			self.checkPPT.setEnabled(True)
			self.checkLPR.setEnabled(True)
		else:
			self.textoCTRT.setText("0")
			self.checkACK.setChecked(False)
			self.checkPPT.setChecked(False)
			self.checkLPR.setChecked(False)
			self.checkACK.setEnabled(False)
			self.checkPPT.setEnabled(False)
			self.checkLPR.setEnabled(False)
			self.checkENQ.setEnabled(False)
			
	def _seleccionarDAT(self, estado):
		if estado == Qt.Checked:
			self.textoDATT.setText("1")
			self.checkCTR.setChecked(False)
			self.checkENQ.setEnabled(True)
		else:
			self.textoDATT.setText("0")
			self.checkENQ.setChecked(False)
			self.checkENQ.setEnabled(False)
			
	def _seleccionarPPT(self, estado):
		if estado == Qt.Checked:
			self.textoPPTT.setText("1")
			self.checkACK.setChecked(False)
			self.checkLPR.setChecked(False)
		else:
			self.textoPPTT.setText("0")
			
	def _seleccionarLPR(self, estado):
		
		if estado == Qt.Checked:
			self.textoLPRT.setText("1")
			self.checkACK.setChecked(False)
			self.checkPPT.setChecked(False)
		else:
			self.textoLPRT.setText("0")
			
	def crear_conexion(self):
		tipo = QInputDialog.getItem(self, "Tipo de usuario", "usuario", ["" ,self._SERVIDOR, self._CLIENTE])
		self.rol = str(tipo[0])
		self.setWindowTitle("Protocolo de transmision de datos  --" + self.rol)
		if self.rol == self._SERVIDOR:
			port = QInputDialog.getInt(self, "ingrese puerto", "Puerto", 56032)
			nom = self.transmisor.crear_servidor(port[0])
			msg = QMessageBox.information(self, "Servidor", "El nombre del servidor es: " + nom)
			del msg
			if self.transmisor.conectar_servidor():
				resp = QMessageBox.information(self, "Conectado", "Se ha establecido la conexion con el cliente")
				del resp
		elif self.rol == self._CLIENTE:
			host = QInputDialog.getText(self, "ingrese host", "Host")
			port = QInputDialog.getInt(self, "ingrese puerto", "Puerto", 56032)
			self.transmisor.conectar_cliente((str(host[0]), port[0]))
		else:
			self.destroy()
			
	def _enviar_mensaje(self):
		self.trama_anterior = self.trama
		if not self.pasos:
			if self.trama.esPPT():			
				self._generar_trama()
				if self.trama.esLPR():
					self.pasos.append("LPR")
					self.transmisor.enviar(self.trama())
					self._mostrar_trama(self._SERVIDOR)
				else:
					err = QMessageBox.information(self, "Error", "Trama fuera de contexto")
					self.trama = self.trama_anterior
			elif self.trama.esNull():
				self._generar_trama()
				if self.trama.esPPT():
					self.pasos.append("PPT")
					self.transmisor.enviar(self.trama())
					self._mostrar_trama(self._SERVIDOR)
				else:
					err = QMessageBox.information(self, "Error", "Trama fuera de contexto")
					self.trama = self.trama_anterior
			else:
				err = QMessageBox.information(self, "Error", "Trama fuera de contexto")
		elif "PPT" in self.pasos:
			if self.trama.esLPR() or self.trama.esACK():
				cant = int(self.textoFramesT.text())
				if not self.mensaje:
					self._preparar_mensaje(cant)
				self._generar_trama()
				if self.trama.esDAT():
					if len(self.mensaje)>1:
						self.trama.INFO = self.mensaje.pop(0)
						self.trama.NUM = str(cant - len(self.mensaje))
						self.transmisor.enviar(self.trama())
						self._mostrar_trama(self._SERVIDOR)
					else:
						err = QMessageBox.information(self, "Error", "Ultima trama, envie ENQ")
						self.trama = self.trama_anterior
						del err
				elif self.trama.esENQ():
					if len(self.mensaje)>1:
						err = QMessageBox.information(self, "Error", "Faltan mas tramas, envie DAT")
						self.trama = self.trama_anterior
						del err
					else:
						self.trama.INFO = self.mensaje.pop(0)
						self.trama.NUM = str(cant)
						self.transmisor.enviar(self.trama())
						self.pasos.append("ENQ")
						self._mostrar_trama(self._SERVIDOR)
			else:
				err = QMessageBox.information(self, "Error", "Trama fuera de contexto")
		elif "LPR" in self.pasos:
			if self.trama.esDAT() or self.trama.esENQ():
				self._generar_trama()
				if self.trama.esACK():
					self.trama.INFO=""
					self.transmisor.enviar(self.trama())
					self._mostrar_trama(self._SERVIDOR)
				else:
					err = QMessageBox.information(self, "Error", "Trama fuera de contexto")
					self.trama = self.trama_anterior
					del err
			else:
				err = QMessageBox.information(self, "Error", "Trama fuera de contexto")

	def _recibir_mensaje(self):
		self.trama_anterior = self.trama
		msg = self.transmisor.recibir()
		if len(msg)!=0:
			datos = list(msg.split(self.trama.INDICADOR)[1])
			self.trama.ACK = datos.pop(0)
			self.trama.ENQ = datos.pop(0)
			self.trama.CTR = datos.pop(0)
			self.trama.DAT = datos.pop(0)
			self.trama.PPT = datos.pop(0)
			self.trama.LPR = datos.pop(0)
			self.trama.NUM = datos.pop(0)
			self.trama.INFO = "".join(datos)
			self._mostrar_trama(self._CLIENTE)
			if self.trama.esDAT():
				self.textoMensajeR.setText(self.textoMensajeR.text()+self.trama.INFO)
			elif self.trama.esENQ():
				self.textoMensajeR.setText(self.textoMensajeR.text()+self.trama.INFO)
				self.pasos.append("ENQ")
		else:
			err = QMessageBox.information(self, "Error", "Mensaje vacio")
			del err

	def _preparar_mensaje(self, cant):
		self.textoMensajeT.setEnabled(False)
		self.textoFramesT.setEnabled(False)
		men = str(self.textoMensajeT.text())
		tam = len(men)/cant + 1
		for i in range(cant):
			self.mensaje.append(men[(i*tam):(i+1)*tam])
		
		
	def _generar_trama(self):
		self.trama.ACK = str(self.textoACKT.text())
		self.trama.ENQ = str(self.textoENQT.text())
		self.trama.CTR = str(self.textoCTRT.text())
		self.trama.DAT = str(self.textoDATT.text())
		self.trama.PPT = str(self.textoPPTT.text())
		self.trama.LPR = str(self.textoLPRT.text())
		self.trama.NUM = str(self.textoNUMT.text())
		self.trama.INFO = str(self.textoInfoT.text())
		
	def _mostrar_trama(self, tipo):
		if tipo == self._CLIENTE:
			self.textoIndicador1R.setText(self.trama.INDICADOR)
			self.textoACKR.setText(self.trama.ACK)
			self.textoENQR.setText(self.trama.ENQ)
			self.textoCTRR.setText(self.trama.CTR)
			self.textoDATR.setText(self.trama.DAT)
			self.textoPPTR.setText(self.trama.PPT)
			self.textoLPRR.setText(self.trama.LPR)
			self.textoNUMR.setText(self.trama.NUM)
			self.textoInfoR.setText(self.trama.INFO)
			self.textoIndicador2R.setText(self.trama.INDICADOR)
		elif tipo == self._SERVIDOR:
			self.textoIndicador1T.setText(self.trama.INDICADOR)
			self.textoACKT.setText(self.trama.ACK)
			self.textoENQT.setText(self.trama.ENQ)
			self.textoCTRT.setText(self.trama.CTR)
			self.textoDATT.setText(self.trama.DAT)
			self.textoPPTT.setText(self.trama.PPT)
			self.textoLPRT.setText(self.trama.LPR)
			self.textoNUMT.setText(self.trama.NUM)
			self.textoInfoT.setText(self.trama.INFO)
			self.textoIndicador2T.setText(self.trama.INDICADOR)
		self._actualizar_semantica(tipo)
	
	
	
	def _actualizar_semantica(self, tipo):
		if tipo == self._CLIENTE:
			if self.trama.esACK():
				self.labelSemanticaR.setText("Semantica: Trama de control, recibio con exito.")
			elif self.trama.esPPT():
				self.labelSemanticaR.setText("Semantica: Trama de control, permiso para transmitir.")
			elif self.trama.esLPR():
				self.labelSemanticaR.setText("Semantica: Trama de control, listo para recibir.")
			elif self.trama.esDAT():
				self.labelSemanticaR.setText("Semantica: Trama de datos.")
			elif self.trama.esENQ():
				self.labelSemanticaR.setText("Semantica: Trama de datos, ultima trama")
			self.labelSemanticaR.adjustSize()
		elif tipo == self._SERVIDOR:
			if self.trama.esACK():
				self.labelSemanticaT.setText("Semantica: Trama de control, recibio con exito.")
			elif self.trama.esPPT():
				self.labelSemanticaT.setText("Semantica: Trama de control, permiso para transmitir.")
			elif self.trama.esLPR():
				self.labelSemanticaT.setText("Semantica: Trama de control, listo para recibir.")
			elif self.trama.esDAT():
				self.labelSemanticaT.setText("Semantica: Trama de datos.")
			elif self.trama.esENQ():
				self.labelSemanticaT.setText("Semantica: Trama de datos, ultima trama")
			self.labelSemanticaT.adjustSize()
