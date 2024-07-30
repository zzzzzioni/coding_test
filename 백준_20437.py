N = int(input())

string = []
num = []
for _ in range(N):
    string.append(list(input()))
    num.append(int(input()))

    
for s in range(N):
    crit = set(string[s])
    st = string[s]
    L = []
    for c in crit:
        if st.count(c) >= num[s]:
            l = []
            for i in range(len(st)):
                if (st[i] == c):
                    l.append(i)
            
            L.append(l)            
    
    cal = []
    for l in L:
        for i in range(len(l)-num[s]+1):
            cal.append(l[i+num[s]-1] -l[i] + 1)
        
    if len(cal) != 0:
        print(min(cal), max(cal)) 
    else:
        print(-1)