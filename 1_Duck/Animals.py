from Items import *


class BaseAnimal:
    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def age(self):
        return self.__age

    # конструктор
    def __init__(self, name: str, age: int):
        self.__name = name  # set name
        self.__age = age  # set age
        self.__hp = 100


class Duck(BaseAnimal):
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, item: BaseItem):
        if item is not None:
            self.__items.append(item)
        else:
            print("Недопустимый возраст")

    def __init__(self, name, age):
        BaseAnimal.__init__(self, name, age)
        self.__items = []

    def display_info(self):
        print(f"Hi, 🦆 my name is {self.name} and Im {self.age} y.o. \n"
              f"Also, you should know I used to karate, so I can break even pinokio by one hit")
