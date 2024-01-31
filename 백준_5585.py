T = int(input())

Z = 1000 - T
a = Z//500
Z = Z - a*500
b = Z//100
Z = Z - b*100
c = Z//50
Z = Z - c*50
d = Z//10
Z = Z - d*10
e = Z//5
Z = Z - e*5

print(a+b+c+d+e+Z)