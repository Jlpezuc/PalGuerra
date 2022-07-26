import imp
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DataBase import DataBase
from PyQt5.QtCore import (Qt, pyqtSignal)

class EmployeeView(QMainWindow):
    
    login_employee_signal = pyqtSignal()
    login_rh_signal = pyqtSignal()

    def __init__(self):
        
        self.db_manager = DataBase()
        super(EmployeeView, self).__init__()
        uic.loadUi("TDA-Project/employeeView.ui", self)
        
        

        
