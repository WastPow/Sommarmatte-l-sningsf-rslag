#Uppgift 3
"""
Primtalsfaktorerna av 13195 är 5, 7, 13 och 29.
Vilken är den största primtalsfaktorn av 600851475143?
"""

#Svar: 6857

num = 600851475143
factors = []

while num > 1:
  for i in range(2,num+1):
    if num % i == 0:
      num = int(num/i)
      factors.append(i)
      break

print(factors)
