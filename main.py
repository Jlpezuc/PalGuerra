from PyQt5.QtWidgets import *
from LoginView import LoginView
from AdminView import AdminView
from EmployeeView import EmployeeView


if __name__ == '__main__':
    
    app = QApplication([])
    login_view = LoginView()
    admin_view = AdminView()
    employee_view = EmployeeView()
    
    login_view.login_rh_signal.connect(admin_view.show)
    login_view.login_employee_signal.connect(employee_view.show)
    
    login_view.show()
    app.exec()