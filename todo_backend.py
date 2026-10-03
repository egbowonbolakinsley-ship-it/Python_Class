import mysql.connector as sql
from pwinput import pwinput

class TodoBackend:
    __name = None
    __database = []
    
    def __init__(self, name):
        self.__name = name
    
    def create_todo(self, todo):
        if not todo:
            return "Todo can't be empty"
        self.__database.append(todo)
        return "Todo added successfully"
    
    def get_todos(self):
        return self.__database
    
    def get_name(self):
        return self.__name
    

class BANK_SQL:
    try:
        
        __conn = sql.connect(
            host = "127.0.0.1",
            user = "root",
            password = "password",
            port = "3306",
            database = "aug26_db"
        )
        __conn.autocommit = True
        __cursor = __conn.cursor()
        
        
    except Exception as e:
        print("Connection Failed:", e)
        exit()
        
    
    def __init__(self):
        pass
    
    def validate_email(self):
        email = input("Email: ").strip().lower()
        if "@" in email and "." in email:
            return email
        
        print("Invalid Email.")
        return self.validate_email()
    

    def login(self):
        email = self.validate_email()
        password = pwinput()
        
        query = "SELECT * FROM customer WHERE email=%s AND password=%s"
        values = (email, password)
        self.__cursor.execute(query, values)
        user = self.__cursor.fetchone()
        
        if user:
            print("Login Successfull")
        else:
            print("Invalid Email or Password")
    

bk = BANK_SQL()
bk.login()