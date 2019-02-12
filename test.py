from answers import revers_sentence
from answers import count_char
from answers import list_filter
"""
print("Zad4")
res = revers_sentence("Python is easy")
print(res)
print("---")
res = revers_sentence("Ala ma kota")
print(res)
"""

"""
print("Zad5")
n = count_char("Ala ma kotA",'a')
print(n) # 4
n = count_char("ala ma kota",'A')
print(n) # 4
n = count_char("Python is easy","a")
print(n) # 0
n = count_char("Jakiś tam sobie text","i")
print(n) # 2
"""


print("Zad6")

result = list_filter([1,8,15,20,11], 20)
print(result) # [1,8,15,11]
result = list_filter([1,8,15,20,11], 20,4)
print(result) # [1,15,11]
result = list_filter([1,8,15,20,11], 2, 5, 31)
print(result) # [1,11]
