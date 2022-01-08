# pythag
# (c) frosDfurret 01/08/22
# this took way too fucking long to make
print('pythag')
print("i'm so fucking tired")
import math
a1, b1 = map(int, input("a1 b1").split())
a2, b2 = map(int, input("a2 b2").split())
c1 = abs(a1-a2)
c2 = abs(b1-b2)
print('(AB)^2 = ('+str(c1)+')^2+('+str(c2)+')^2')
c1 = pow(c1,2)
c2 = pow(c2,2)
f = c1+c2
print('(AB)^2 = '+str(f))
print('AB = √('+str(f)+')')
f = math.sqrt(f)
print('AB = '+str(f))
print('copy the above for ezpz ok bye loser')
