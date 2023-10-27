#мій класом
class Employee:
        name = ""
        age = 0
        profession = ""
        education = ""
employee1 = Employee()
employee1.name = "Ivan"
employee1.age = 35
employee1.profession = "Computer programmer"
employee1.education = "Master"

print(employee1.name, employee1.age, employee1.profession, employee1.education)

employee1.age = 37
print(employee1.name, employee1.age, employee1.profession, employee1.education)


#мій класс з конструктором
class Worker:
    def __init__(self, name, age, profession, education):
        self.name = name
        self.age = age
        self.profession = profession
        self.education = education
roma = Worker("Roma", 28, "engineer", "Master")
print(roma.name, roma.age, roma.profession, roma.education)
roma.age = 30
print(roma.name, roma.age, roma.profession, roma.education)
