# import todo_backend
# from todo_backend import TodoBackend, Hello
from todo_backend import TodoBackend as TB, Hello




class TodoFrontend(TB):
    
    def home(self):
        print(f"""
            Welcome to {self.get_name()}
              
        1. Add Todo
        2. View all
        #. Exit     
        """)
        
        choice = input("Choice: ")
        if choice == "1":
            self.add_todo()
        elif choice == "2":
            self.view_all()
        elif choice == "#":
            exit("Goodbye!")
        else:
            print("Invalid option")
            self.home()
        
    def add_todo(self):
        todo = input("Todo: ")
        res = self.create_todo(todo)
        print(res)
        self.home()
        
    def view_all(self):
        todos = self.get_todos()
        print(todos)
        self.home()
        
my_app = TodoFrontend("MyApp")
my_app.home()