Cond = list(map(int, input().split(' ')))

Roads = []

for _ in range(Cond[0]):
    Roads.append(list(map(int, input().split(' '))))

Fin = []
for road in Roads:
    if road[1] > Cond[1]:
        pass        
    else:
        if (road[1] - road[0]) <= road[2]:
            pass
        else:
            Fin.append([road[0], road[1], road[2], road[2]/(road[1] - road[0])])
        
Fin.sort(key=lambda x : x[3])

l = 0
Whole = list(range(1, Cond[1] + 1))
for r in Fin:
    try:
        if len(Whole[Whole.index(r[0]+1):Whole.index(r[1])+1]) == (r[1]-r[0]):
            if r[1] == Cond[1]:
                del Whole[Whole.index(r[0]+1):]
                l += r[2]
            else:
                del Whole[Whole.index(r[0]+1):Whole.index(r[1])+1]
                l += r[2]
        else:
            pass
    except:
        pass

print(l + len(Whole))



