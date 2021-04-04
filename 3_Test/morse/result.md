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

