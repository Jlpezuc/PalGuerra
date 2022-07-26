import imp
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DataBase import DataBase
from PyQt5.QtCore import (Qt, pyqtSignal)

class LoginView(QMainWindow):
    
    login_employee_signal = pyqtSignal()
    login_rh_signal = pyqtSignal()

    def __init__(self):
        
        self.db_manager = DataBase()
        super(LoginView, self).__init__()
        uic.loadUi("TDA-Project/LoginView.ui", self)
        
        self.b_login.clicked.connect(self.verify_login)
    
    def verify_login(self):
        if self.db_manager.user_exist(self.input_rut.text(), self.input_password.text()):
            print("existe")
            if self.db_manager.user_type(self.input_rut.text(), self.input_password.text()) == 1:
                self.login_rh_signal.emit()
            else:
                self.login_employee_signal.emit()
            self.close()
        else:
            self.input_rut.setText("Usuario Invalido")
