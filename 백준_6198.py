# 전혀 모르겠음 ㅠㅠ ...너무 슬프다 ㅠㅠㅠ .... 


N = int(input())

B = []
for h in range(N):
    B.append(int(input()))

# 강아지's CODE
temp = []
output = 0

for h in B:
    
    while temp and temp[-1] <= h:
        temp.pop()

    temp.append(h)
   
    output += len(temp) - 1

result = output

print(result)