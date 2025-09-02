import random
class Student:
    def __init__(self, name, trait):
        self.name = name
        self.trait = trait
        self.school = ""

    def get_school(self):
        if self.trait =="brave":
            self.school= "Gryffindor"
        elif self.trait=="loyal":
            self.school="Huttiepuff"
        elif self.trait=="wise":
            self.school="Ravendaw"
        elif self.trait=="cunning":
            self.school="Slythenn"
        else:
            self.school=random
        print(f"Your name is {self.name}, Your school is {self.school} ")
Student1=Student("dareen", "loyal")
Student1.get_school()
Student2=Student("Razan","cute")
Student2.get_school()