from my_package import lesson1 as l1
from my_package import lesson2 as l2
from my_package import lesson3 as l3
import emoji


print(emoji.emojize("Python is fun :snake: "))


l1.hello()
l2.greet()
l3.welcome()


# from math import sqrt as sq
# import importlib
#
# import lesson5.py
#
# importlib.reload(lesson5.py)
#
#
# result = sq(25)
# print(result)