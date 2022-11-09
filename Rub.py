from PyQt5.QtCore import pyqtSignal, QObject

class Ruble(QObject):
    setRuble = pyqtSignal(int)

    def __init__(self, r):
        super().__init__()
        self.rub = r

    def change(self, n):
        if n > 0:
            self.rub = self.rub * 2*n
        else:
            self.rub = self.rub / (2*(-n))

    def getRuble(self):
        return str('{:.6f}'.format(self.rub))