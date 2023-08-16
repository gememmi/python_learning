import random as r
import time as t
from typing import List

print("HELLO WORLD!")

me = "Emily"
randomArr = ["Roman", 4, "Noelia", 8, True] 

alphabet = ["a", "b", "c", "d", "e", "f"]

if me=="Emily":
    print("hello " + me)



for i in range(5):
    var = str(i+1)+". "
    var1 = 0
    var2 = ""
    print(var)
    for j in randomArr:
        randy = r.randint(0,len(randomArr)-1)
        var2 += str(randomArr[randy]) + " "
        var3 = alphabet[var1] + ". " + var2
        var1 += 1
        print(var3)

# print(t.localtime()[0])

k = 0

while k < 5:
    var = str(k+1) + ". "
    k+=1
    var1 = 0
    var2 = ""
    print(var)
    m = 0
    while m < len(randomArr):
        var2 += str(randomArr[randy]) + " "
        var3 = alphabet[var1] + ". " + var2
        var1 += 1   
        m += 1
        print(var3)
        
