L = list(map(int, input().split()))
T = list(map(int, input().split()))

R = []
c = 0

for i in range(len(T)):
    if (sum(R) + T[i]) <= L[2]:
        R.append(T[i])
        c += 1
        if len(R) > L[1]:
            del R[0]
        
    else:
        while len(R) != L[1]:
            R.append(0)
            c += 1 
        
        while (sum(R[1:]) + T[i]) > L[2]:
            del R[0]
            R.append(0)
            c += 1
    
        del R[0]
        R.append(T[i])
        c += 1   

    if i == (len(T)-1):
        c += L[1]

print(c)



