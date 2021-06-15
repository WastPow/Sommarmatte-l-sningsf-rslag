#Uppgift 7

"""
Vad är siffersumman av 2¹⁰⁰⁰?
"""

#Svar: 1366


siffersumma = 0
num = 2**1000

for number in str(num):
  siffersumma += int(number)

print(siffersumma)
