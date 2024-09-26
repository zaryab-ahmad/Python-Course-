class Student:
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def infro(self):
        return f"Student name  {self.name}, student ID {self.id}"