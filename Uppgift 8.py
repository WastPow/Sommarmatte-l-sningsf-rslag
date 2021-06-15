"""
Uppgift 8a)
Vilket index har det första fibonacci tal som innehåller 100 siffror?
"""

#Svar: 4782

fib1 = 1
fib2 = 1
fib2_index = 2
while len(str(fib2)) < 1000:
  fib1, fib2 = fib2, fib1 + fib2
  fib2_index += 1
print(fib2_index)

"""
Uppgift 8b)
Vad blir kvoten Fn+1/Fn då?
"""

#Svar: 1.618033988749895 (Jämför med det gyllene snittet!)

fib1 = 1
fib2 = 1
fib2_index = 2
while len(str(fib2)) < 1000:
  fib1, fib2 = fib2, fib1 + fib2
  fib2_index += 1

print(fib2/fib1)
