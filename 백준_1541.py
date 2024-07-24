##################
######GREEDY######
##################
# 문제에서 나타난 힌트 : '이 식의 값을 <최소>로 만드는 프로그램'

I = input()

# input 받는 부분이 정말 힘들었다 ;;;;;;;;;;;;
S = []
num =''
for i in range(len(I)):
    if I[i] in ['+', '-']:
        S.append(num)
        S.append(I[i])
        num = ''
    else:
        num += I[i]
S.append(num)

cnt = 0
div = True
for i in S:
    if i == '-':
        div = False
    elif i == '+':
        pass
    else:
        if div:
            cnt += int(i)
        else:
            cnt -= int(i)

print(cnt)