```buildoutcfg
pip install coverage
```
```buildoutcfg
coverage run -m pytest
```
```commandline
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.7.8, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\user\Desktop\TasksAvitoPython\3_Test\what_is_year_now
plugins: Faker-6.5.2
collected 3 items                                                                                                                                                                                                                         

test_what_is_year_now.py ...                                                                                                                                                                                                        [100%]

=========================================================================================================== 3 passed in 0.21s ============================================================================================================

```
```buildoutcfg
coverage report -m
```
```commandline
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
test_what_is_year_now.py      25      0   100%
what_is_year_now.py           19      0   100%
--------------------------------------------------------
TOTAL                         44      0   100%
```
```buildoutcfg
coverage html
```
```dtd
htmlcov/index.html
```