"""
Genom att göra en lista på de sex första primtal får vi en lista på 2,3,5,7,11, och 13. Vi kan därmed se att 13 är det sjätte primtalet. Vilket är det 10 001 primtalet?
"""
#Svar: 104743

num = 3
primes = [2]
while len(primes) < 10001:
  for i in range(2,num):
    if num % i == 0:
      break
  if i == num-1:
    primes.append(num)
  num += 1

print(primes[-1])
