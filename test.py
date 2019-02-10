import answers
from answers import count_char
"""
print("Zad4")
res = answers.revers_sentence("Python is easy")
print(res)
print("---")
res = answers.revers_sentence("Ala ma kota")
print(res)
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

