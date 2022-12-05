import random


class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show(self):
        print(f"My name is {self.name} and I'm {self.age} years old. My fur is {self.color}.")

    def get_name(self):
        return self.name


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(self, name, age)
        self.name = name
        self.age = age
        self.color = color


class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(self, name, age)
        self.name = name
        self.age = age
        self.color = color


c = Cat("Fluffy", 10, "red")
c.show()
d = Dog("Lucky", 9, "orange")
d.show()

animals = [c, d]
lines = [
    " don't like you and proceeds to bite you to death",
    " like you a bit and let you pet him",
    " like you and show his family"
]

for i in animals:
    print(i.get_name() + lines[random.randint(0, len(lines) - 1)])
