import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from analizadorSintacticoSQL import validar

qtCreatorFile = './view/viewMain.ui' #Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        
        self.setWindowTitle('.:: ANALIZADOR SINTACTICO::. ')
        self.setFixedSize(770, 300)
        
        self.btnAnalizar.clicked.connect(self.validacion)
        self.btnSalir.clicked.connect(self.salir)
    
    def validacion(self):            
        cadenaTexto = self.obtenerCadena()
        
        # if cadenaTexto[-2:]
        if not cadenaTexto:
            QMessageBox.warning(None, 'vacio', 'Campo vacio')
        else:
            valido = validar(cadenaTexto)
            if valido:
                self.lblAnalisis.setText('SENTENCIA CORRECTA')
                QMessageBox.information(None, 'Validación', '¡¡La Sentencia SQL ingresada es valida!!')
            else:
                self.lblAnalisis.setText('SENTENCIA INCORRECTA')
                QMessageBox.critical(None, 'Validación', '¡¡La Sentencia SQL ingresada no es valida!!')
    
    
    def obtenerCadena(self):
        cadenaTexto = self.cadena.text()
        print(cadenaTexto)
        return cadenaTexto

    

    def salir(self):
        salir = QMessageBox.question(
            self, 'Salir', '¿Esta seguro/a de salir?', QMessageBox.Yes, QMessageBox.No)
        if salir == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())