import sys

S = sys.stdin.readline().rstrip()

L = [ S[i:] for i in range(len(S))]
L.sort()

for l in L:
    print(l)