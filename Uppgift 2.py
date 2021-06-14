#Uppgift 2
"""
Summan av de tio första naturliga talens kvadrater är 12+22+...+102= 385
Summan av de tio första naturliga talen i kvadrat är (1+2+...+10)2=552=3025
Därmed är differensen av summorna 3025-385=2640.
Beräkna differensen mellan summan av alla naturliga tals kvadrater från 1 → 100 och kvadraten av summan från alla tal mellan 1 → 100.

"""

#Svar: 25164150

tal1 = 0
for i in range(101):
  tal1 += i**2

tal2 = 0
for i in range(101):
  tal2 += i
tal2 = tal2**2

print(tal2-tal1)
