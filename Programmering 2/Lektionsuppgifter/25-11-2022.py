class Person:
    def __init__(self, name, age, role, salery):
        self.name = name
        self.age = age
        self.role = role
        self.salery = salery

    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old. "
              f"I am {self.role} and I earn {self.salery} dollars per month \n")


class Company:
    def __init__(self, name, founded, humanrightsviolated):
        self.name = name
        self.founded = founded
        self.humanrightsviolated = humanrightsviolated

    def show(self):
        print(f"This company is called {self.name}. It was founed in {self.founded}"
              f" and committed {self.humanrightsviolated} human rights violations last year alone! Very good."
              f" Here are the workers: \n")


class CEO(Person):
    def __init__(self, name, age, role, salery):
        super().__init__(name, age, role, salery)
        self.role = role
        self.salery = salery


class Worker:
    def __init__(self, name, age, role, salery):
        self.name = name
        self.age = age
        self.role = role
        self.salery = salery

    def show(self):
        print(
            f"My name is {self.name} and I am {self.age} years old. I was {self.role}"
            f" and I get {self.salery} per day. \n")


class Assistant(Person):
    def __init__(self, name, age, role, salery):
        super().__init__(name, age, role, salery)
        self.role = role
        self.salery = salery


class Intern(Person):
    def __init__(self, name, age, role, salery):
        super().__init__(name, age, role, salery)
        self.role = role
        self.salery = salery


class Receptionist(Person):
    def __init__(self, name, age, role, salery):
        super().__init__(name, age, role, salery)
        self.role = role
        self.salery = salery


print("\n")

s = Company("APPuru Ab", "1946", "433")
s.show()
c = CEO("Job", 29, "the CEO", "500.000")
c.show()
w = Worker("John", 9, "sentenced to hard labour for 57 years", "half a piece of bread and a glass of water")
w.show()
a = Assistant("Stacey", 18, "an assistant", "1500")
a.show()
i = Intern("Steve", 73, "an intern", "2000")
i.show()
r = Receptionist("Jessica", 43, "a receptionist", "1000")
r.show()
