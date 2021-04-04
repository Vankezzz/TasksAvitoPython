#Тестирование модуля реализующего декодирование и кодирование сигнала азбуки Морзе
## issue-01
Дана функция, кодирующая строку в соответсвии с таблицей азбуки Морзе

```python
# полный код в файле morse.py
def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
```

Напишите на неё тесты с использование `doctest`

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* используется директива
* используется флаг
* тест с message = 'SOS'
* тест с исклечением (Exception)
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и доктестами
* нет замечаний от `flake8`

## Solution of issue-01 
Для запуска doctest нужно запустить модуль morse.py в соответствующем режиме и с флагом NORMALIZE_WHITESPACE 
```buildoutcfg
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```
Результаты теста:
```python
Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    decode(".--. .. -. -.-. ....") # doctest: +ELLIPSIS
Expecting:
    'PINCH'
ok
Trying:
    decode('------')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: '------'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode("PINCH") # doctest: +ELLIPSIS
Expecting:
    '.--. ... ....'
ok
Trying:
    encode('z')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 'z'
ok
1 items had no tests:
    morse
2 items passed all tests:
   3 tests in morse.decode
   3 tests in morse.encode
6 tests in 3 items.
6 passed and 0 failed.
Test passed.
```

## issue-02
Дана функция, декодирующая строку из азбуки Морзе в английский

```python
# полный код в файле morse.py
def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)
```

Напишите на неё параметрический тест, используя `pytest.mark.parametrize`

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 3 тестовых примера
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`

## Solution of issue-02
Для запуска параметрического теста, скрипт которого содержится в  morse_test.py, нужно запустить с помощью утилиты pytest
```buildoutcfg
pytest morse_test.py
```
Результаты теста:
```python
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.7.8, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\user\Desktop\TasksAvitoPython
plugins: Faker-6.5.2
collected 4 items                                                                                                                                                                                                                         

3_Test\morse\morse_test.py ....                                                                                                                                                                                                     [100%]

=========================================================================================================== 4 passed in 0.10s ============================================================================================================
```