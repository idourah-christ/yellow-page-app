from abc import ABC,abstractclassmethod

class Employee():

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    @abstractclassmethod
    def get_salary(self):
        pass 

    @abstractclassmethod
    def show_description(self):
        pass 

class Developer(Employee):

    def __init__(self, name, salary, languages, position):
        super().__init__(name, salary)
        self.languages = languages
        self.position = position

    def get_salary(self):
        work_bonus = self.salary * 0.5
        return self.salary + work_bonus

    def show_description(self):
        print(
        f""" 
        My name is {self.name} a developer working as a {self.position} 
        my salary is {self.get_salary()} and I know {self.languages}
        """)

class Manager(Employee):

    def __init__(self, name, salary, experience):
        super().__init__(name, salary)
        self.experience = experience 

    def get_salary(self):
        bonus = self.salary * 5.0
        return self.salary + bonus 

    def show_description(self):
        print(f"""
        My name is {self.name} I am Manager and have {self.experience}
        my salary is {self.get_salary()}.
        """) 

class CompositeEmployee:

    def __init__(self):
        self.employees = []

    def add(self, emp):
        self.employees.append(emp)

    def remove(self, emp):
        self.employees.remove(emp)

    def show_description(self):
        for emp in self.employees:
            emp.show_description()

dev = Developer('idourah christ',2000,['python','C++','Java'],'DevOps engineer')
dev1 = Developer('Jessica colombe',450,['Angular','Vues'],'Front end Developer')
manag = Manager("Yoane",5000,5)

employess = CompositeEmployee()
employess.add(dev)
employess.add(manag)
employess.add(dev1)
employess.show_description()