class BaseItem:
    @property
    def name(self):
        return self.__name

    # конструктор
    def __init__(self, name, age):
        self.__name = name  # set name


class Umbrella(BaseItem):
    def __init__(self, name: str):
        BaseItem(self, name)


class Doggy(BaseItem):
    def __init__(self, name: str):
        BaseItem(self, name)


class Ventuz(BaseItem):
    def __init__(self, name: str):
        BaseItem(self, name)
