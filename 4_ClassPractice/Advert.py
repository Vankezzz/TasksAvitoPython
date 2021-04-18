import json
import keyword


class ColorizeMixin:
    """
    Print title and price attribute
     033 - Escape-code
    3 = style of text.
    31 = foreground of text
    42 м = background of text
    """
    foreground_code = 31
    background_code = 42
    style_code = 3

    def __repr__(self):
        return f'\033[{self.style_code};{self.foreground_code};{self.background_code}m ' \
               f'{self.title} | {self.price} ₽' \
               f'\033[0;1;1m'


class Advert(ColorizeMixin):
    """
    Contains advert info
    """
    _price = 0

    def __setattr__(self, key, value):
        if keyword.iskeyword(key):
            key = key + "_"
        super.__setattr__(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, var: int):
        if var < 0:
            raise ValueError("must be >= 0")
        self._price = var


def get_obj_from_json(data: dict, cls: object) -> object:
    """
    Convert dict to object
    :param data: dict
    :param cls: class description
    :return: object ob cls
    """
    obj = cls()
    for a, b in data.items():
        if isinstance(b, (list, tuple)):
            obj.__setattr__(a, [get_obj_from_json(x, cls)
                                if isinstance(x, dict)
                                else x for x in b])
        else:
            obj.__setattr__(a, get_obj_from_json(b, cls)
            if isinstance(b, dict) else b)
    return obj


lesson_str = """{
  "title": "Вельш-корги",
  "price": 1000,
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

if __name__ == '__main__':
    lesson = json.loads(lesson_str)
    corgi = get_obj_from_json(lesson, Advert)
    print(corgi.class_)
    print(corgi)
    print(corgi.location.address)
