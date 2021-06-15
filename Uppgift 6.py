#Uppgift 6
"""
Hitta det heltal (under 1.000.000) som ger den längsta kedjan i Collatz nummerlek
"""

#Svar: 837799

biggest_num = 0
biggest_chain = 0
for i in range(1,1000001):
  num = i
  curr_chain = 0
  while num != 1:
    if num % 2 == 0:
      num /= 2
    elif num % 2 == 1:
      num = 3*num + 1
    curr_chain += 1
  if curr_chain > biggest_chain:
    biggest_chain = curr_chain
    biggest_num = i

print(biggest_num)
