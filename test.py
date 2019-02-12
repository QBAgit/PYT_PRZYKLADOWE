
"""
from answers import revers_sentence
print("Zad4")
res = revers_sentence("Python is easy")
print(res)
print("---")
res = revers_sentence("Ala ma kota")
print(res)
"""

"""
from answers import count_char
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

"""
from answers import list_filter
print("Zad6")

result = list_filter([1,8,15,20,11], 20)
print(result) # [1,8,15,11]
result = list_filter([1,8,15,20,11], 20,4)
print(result) # [1,15,11]
result = list_filter([1,8,15,20,11], 2, 5, 31)
print(result) # [1,11]
"""

from answers import get_random_elements
print("Zad7")
result = get_random_elements([1,2,6,3,7])
print(result) # [2]
result = get_random_elements([1,2,6,3,7],3) 
print(result)# [6,2,7]
result = get_random_elements([1,2,6,3,7],5) 
print(result)# [6,2,7]


try:
    result = get_random_elements([1,2,6,3,7],3.14) 
    print(result)# Wyjątek!
except Exception as e:
    print(str(e))


try:
    result = get_random_elements([1,2,6,3,7],-1) 
    print(result)# Wyjątek!
except Exception as e:
    print(str(e))

try:
    result = get_random_elements([1,2,6,3,7],6) 
    print(result)# Wyjątek!
except Exception as e:
    print(str(e))
