from PyQt5.QtCore import pyqtSignal, QObject

class Dollar(QObject):
    setDollar = pyqtSignal(int)

    def __init__(self, d):
        super().__init__()
        self.dollar = d

    def change(self,n):
        if n > 0:
            self.dollar = self.dollar * 2*n
        else:
            self.dollar = self.dollar / (2*(-n))

    def getDollar(self):
        return str('{:.6f}'.format(self.dollar))