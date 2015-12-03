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
		
		self.labelSemanticaT = QLabel("Semantica: ")
		self.labelSemanticaR = QLabel("Semantica: ")
		self.labelSemanticaT.adjustSize()
		self.labelSemanticaR.adjustSize()
		
		#campos de texto transmisor
		self.textoMensajeT = QLineEdit()
		self.textoFramesT = QLineEdit()
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
		self.textoHeaderR = QLineEdit()
		self.textoCamposR = QLineEdit()
		self.textoInformacionR = QLineEdit()
		self.textoTrailerR = QLineEdit()
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
		self.botonRespuesta = QPushButton("RESPONDER")
		self.trama = Trama()
		self.transmisor = Transmisor()
		self._inicializar()
		
		
	def _inicializar(self):
		self.setWindowTitle("Protocolo de transmision de datos")
		
		#------------------------------------#
		#		ELEMENTOS DEL TRANSMISOR	 #
		#------------------------------------#
		
		#Etiquetas transmisor
		tituloT = QLabel("TRANSMISOR")
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
		tituloR = QLabel("RECEPTOR")
		labelFrameR = QLabel("Trama recibida:")
		labelHeaderR = QLabel("HEADER")
		labelInformacionR = QLabel("INFORMACION")
		labelTrailerR = QLabel("TRAILER")
		labelRespuestaR = QLabel("Respuesta: ")
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
		labelHeaderR.adjustSize()
		labelInformacionR.adjustSize()
		labelTrailerR.adjustSize()
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
		fila7 = QHBoxLayout()
		fila8 = QHBoxLayout()
		fila9 = QHBoxLayout()
		fila10 = QHBoxLayout()
		fila11 = QHBoxLayout()
		cajaReceptor = QVBoxLayout()
		
		fila7_1A = QHBoxLayout()
		fila7_1 = QVBoxLayout()
		fila7_2 = QVBoxLayout()
		fila7_3 = QVBoxLayout()
		
		fila7_1A.addWidget(self.textoHeaderR)
		fila7_1A.addWidget(self.textoCamposR)
		fila7_1.addLayout(fila7_1A)
		fila7_1.addWidget(labelHeaderR)	
		fila7_2.addWidget(self.textoInformacionR)
		fila7_2.addWidget(labelInformacionR)
		fila7_3.addWidget(self.textoTrailerR)
		fila7_3.addWidget(labelTrailerR)
		
		fila5.addWidget(tituloR)
		fila6.addWidget(labelFrameR)
		fila7.addLayout(fila7_1)
		fila7.addLayout(fila7_2)
		fila7.addLayout(fila7_3)
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
		fila9.addWidget(self.botonRespuesta)
		
		fila10.addWidget(self.labelSemanticaR)
		fila11.addWidget(labelMensajeR)
		fila11.addWidget(self.textoMensajeR)
		
		cajaReceptor.addLayout(fila5)
		cajaReceptor.addLayout(fila6)
		cajaReceptor.addLayout(fila7)
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
		
		self.textoHeaderR.setEnabled(False)
		self.textoCamposR.setEnabled(False)
		self.textoInformacionR.setEnabled(False)
		self.textoTrailerR.setEnabled(False)
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
		self.botonRespuesta.clicked.connect(self._enviar_respuesta)
		
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
		if str(tipo[0]) == self._SERVIDOR:
			port = QInputDialog.getInt(self, "ingrese puerto", "Puerto", 56032)
			self.transmisor.crear_servidor(port[0])
			if self.transmisor.conectar_servidor():
				resp = QMessageBox.information(self, "Conectado", "Se ha establecido la conexion con el cliente")
			self.setWindowTitle("Protocolo de transmision de datos  --" + self._SERVIDOR)
		elif str(tipo[0]) == self._CLIENTE:
			host = QInputDialog.getText(self, "ingrese host", "Host")
			port = QInputDialog.getInt(self, "ingrese puerto", "Puerto", 56032)
			self.transmisor.conectar_cliente((str(host[0]), port[0]))
			self.setWindowTitle("Protocolo de transmision de datos  --" + self._CLIENTE)
		else:
			self.destroy()
			
	def _enviar_mensaje(self):
		self.transmisor.enviar(self.trama())
		
	def _enviar_respuesta(self):
		print self.transmisor.recibir()
		
