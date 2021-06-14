#Uppgift 1
"""
Om vi gör en lista på alla naturliga tal mindre än 10 som är multiplar av 3 och 5 så får vi talen 3, 5, 6 och 9. Summerar vi dessa multiplar får vi talet 23. 
Summera alla tal under 1000 som är multiplar av 3 eller 5.
"""
#Svar: 233168

num_list = []
for i in range(1000):
  if i % 3 == 0: 
    num_list.append(i)
  elif i % 5 == 0:
    num_list.append(i)

print(sum(num_list))
