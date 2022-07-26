import imp
from turtle import update
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DataBase import DataBase
from PyQt5.QtCore import (Qt, pyqtSignal)

class AdminView(QMainWindow):
    
    login_employee_signal = pyqtSignal()
    login_rh_signal = pyqtSignal()

    def __init__(self):
        
        self.db_manager = DataBase()
        super(AdminView, self).__init__()
        uic.loadUi("TDA-Project/adminView.ui", self)
        self.pushButton_2.clicked.connect(self.crear_employee)
        self.tableWidget.setRowCount(40)
        self.update_table()
    
    def update_table(self):
        results = self.db_manager.users()
        tableRow = 0
        for row in results:
            sexo = "Vagina"
            if row[3] == 1:
                sexo = "Pene"
            self.tableWidget.setItem(tableRow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tableRow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableRow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tableRow, 3, QTableWidgetItem(sexo))
            self.tableWidget.setItem(tableRow, 4, QTableWidgetItem(row[4]))
            tableRow += 1
    
    def crear_employee(self):
        rut = self.in_rut.text()
        nombre = self.in_nombre.text()
        apellido = self.in_apellido.text()
        sexo = self.in_sexo.text()
        numero = self.in_numero.text()
        cargo = self.in_cargo.text()
        self.db_manager.crear_employee(rut, nombre, apellido, sexo, numero, cargo)
        self.in_rut.setText("")
        self.in_nombre.setText("")
        self.in_apellido.setText("")
        self.in_sexo.setText("")
        self.in_numero.setText("")
        self.in_cargo.setText("")
        self.update_table()
        

