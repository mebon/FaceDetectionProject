from PyQt5.QtWidgets import* #PyQt5 5.10.1 ile çalışıyor.
#from PyQt5.uic import loadUi #pyuic5 ile dönüştürme yaptığımız için ihtiyaç kalmadı.

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        #loadUi("ArayuzTasarimi.ui",self) #pyuic5 ile dönüştürme yaptığımız için ihtiyaç kalmadı.

uygulama = QApplication([])
pencere = main()
pencere.show()
uygulama.exec_()