from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget,QLineEdit,QVBoxLayout,QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from Dollar import Dollar
from Oil import Oil
from Rub import Ruble

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        pixmap = QtGui.QPixmap("img.png").scaled(
            350, 350, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)

        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        self.setPalette(pal)
        self.setMask(pixmap.mask())

        self.oil = Oil(1)
        self.rub = Ruble(97.68 * 61.24)
        self.rub.setRuble.connect(self.rub.change)
        self.dollar = Dollar(97.68)
        self.dollar.setDollar.connect(self.dollar.change)

        self.setWindowTitle("Second lab")
        self.setFixedSize(QSize(300, 400))

        self.label1 = QLabel("Нефть",self)
        self.label1.move(20, 10)

        self.label2 = QLabel("Рубли", self)
        self.label2.move(20, 60)

        self.label3 = QLabel("Доллары", self)
        self.label3.resize(200, 30)
        self.label3.move(20, 110)

        self.fg1 = QLineEdit(self)
        self.fg1.move(160, 10)
        self.fg1.setText(self.oil.getOil())

        self.fg2 = QLineEdit(self)
        self.fg2.move(160, 60)
        self.fg2.setText(self.rub.getRuble())
        self.fg2.setReadOnly(True)

        self.fg3 = QLineEdit(self)
        self.fg3.move(160, 110)
        self.fg3.setText(self.dollar.getDollar())
        self.fg3.setReadOnly(True)

        self.button = QPushButton("Push me ", self)
        self.button.resize(100, 100)
        self.button.move(90, 200)
        self.button.clicked.connect(self.clicked)


    def clicked(self):
        if(float(self.fg1.text())<=0):
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Значение должно быть больше 0')
            self.fg1.setText(self.oil.getOil())
        elif(float(self.fg1.text())>float(self.oil.getOil())):
            f=float(self.fg1.text())-float(self.oil.getOil())
            self.rub.setRuble.emit(-1*(f))
            self.fg2.setText(self.rub.getRuble())

            self.dollar.setDollar.emit(f)
            self.fg3.setText(self.dollar.getDollar())
        elif(float(self.fg1.text())<float(self.oil.getOil())):
            f = -float(self.fg1.text()) + float(self.oil.getOil())
            self.dollar.setDollar.emit(-1*f)
            self.fg3.setText(self.dollar.getDollar())

            self.rub.setRuble.emit(f)
            self.fg2.setText(self.rub.getRuble())


        self.oil.setOil(self.fg1.text())

app = QApplication([])
app.setStyleSheet("QLabel{font-size: 16pt;}")

window = MainWindow()
window.show()

app.exec()