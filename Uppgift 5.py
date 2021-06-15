#Uppgift 5
"""
En pythagoreisk triplett är 3 heltal där a < b < c och a²+b²=c². Det finns exakt 1 pythagoreisk triplet där a+ b + c = 1000. Vad är produkten av abc då a+b+c=1000.
"""
#Svar: 31875000

num1 = 0
num2 = 0
num3 = 0
for a in range(1,1001):
  for b in range(a,1001):
    for c in range(b,1001):
      if a**2+b**2 == c**2:
        if a+b+c == 1000:
          num1 = a
          num2 = b
          num3 = c

print(num1*num2*num3)
