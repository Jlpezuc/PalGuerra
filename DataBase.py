import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456789',
            db='correo_yury'
        )
        
    
    def show_log_action(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM log_action"
        try:
            cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    
    def user_exist(self, username, password):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM employee WHERE rut = '{username}' AND pass = '{password}'"
        try:
            cursor.execute(query)
            return cursor.fetchone() != None
        except Exception as e:
            print(e)
    
    def user_type(self, username, password):
        cursor = self.connection.cursor()
        query = f"SELECT rh FROM employee WHERE rut = '{username}' AND pass = '{password}'"
        try:
            if self.user_exist(username, password):
                cursor.execute(query)
                return cursor.fetchone()[0]
            else:
                return None
        except Exception as e:
            print(e)
    
    def users(self):
        cursor = self.connection.cursor()
        query = f"SELECT rut, first_name, last_name, male, phone FROM employee"
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(e)
    
    def crear_employee(self, rut, nombre, apellido, sexo, numero, cargo):
        cursor = self.connection.cursor()
        male = 0
        if sexo == "hombre":
            male = 1
        rh = 0
        if cargo == "admin":
            rh = 1
        query = f"INSERT INTO employee (rut, first_name, last_name, male, phone, rh) VALUES ('{rut}', '{nombre}', '{apellido}', '{male}', '{numero}', '{rh}')"
        try:
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e)

# if __name__ == '__main__':
#     database = DataBase()

#     # for element in database.show_log_action():
#     #     print(f"id: {element[0]}, description: {element[1]}")
#     print(database.users())