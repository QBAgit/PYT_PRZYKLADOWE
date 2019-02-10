"""
#### Zadanie 4. (2pkt)

Napisz funkcję `revers_sentence`, która przyjmie dowolnie długi napis, 
po czym zwróci napis będący odwróconym zdaniem z zamianą na dużą literę wszystkich pierwszych liter słów.
przykład:

```python
rev = revers_sentence("Ala ma kota")
print(rev) # Atok Am Ala
```

```python
rev = revers_sentence("Python is easy")
print(rev) # Ysae Si Nohtyp
```
"""

def upFirstChar(word):
    out = ""
    for i in range(0,len(word)):
        if i==0:
            mychar = word[0].upper()
        else:
            mychar = word[i].lower()
        out+=mychar
    return out

def revers_sentence(text):
    
    newtext = ""
    #Split by space
    L_text = text.split(" ")
    #Reverse sentence
    L_rev_text = L_text[::-1]

    for word in range(0,len(L_rev_text)):
        #Reverse single word
        rev_word = L_rev_text[word][::-1]
        #Upper First char
        new_word = upFirstChar(rev_word)
        
        #Create new sentence
        newtext += new_word
        # Spaces only inside the sentance
        if (word<len(L_rev_text)-1):
            newtext += " "
        
    return newtext

"""
#### Zadanie 5. (3pkt)

Napisz funkcję `count_char`, która pobierze dowolnie długi łańcuch tekstowy 
oraz pojedynczy znak i sprawdzi, ilość wystąpień podanego znaku. 
Funkcja powinna zliczać znaki niezależnie od ich wielkości, 
tj. znaki `a` oraz `A` powinny być traktowane jako to samo! 

przykład:
```python
n = count_char("Ala ma kotA",'a')
print(n) # 4
n = count_char("ala ma kota",'A')
print(n) # 4
n = count_char("Python is easy",'a')
print(n) # 0
```
##### Podpowiedź: zawsze możesz najpierw sprowadzić oba podane napisy do dużych lub małych liter!
    
"""

def count_char(text,x):

    ctr=0

    for myitem in text:
        if (myitem.lower() == x.lower()):
            ctr+=1

    return ctr
