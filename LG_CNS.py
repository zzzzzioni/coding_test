"""
    1번 문제: 차 구간 단속
구간단속이 여러개 주어진다.
이때, 단 한개의 구간단속에도 걸리지 않는 차의 수를 출력하라.

- inclusive. 즉, 단속구간이 80부터 100이면 80과 100은 통과.

input:

> 구간단속 N개, 지나가는 차 Q개
N만큼의 구간단속이 줄마다 하나씩 나온다
Q개 차가 줄마다 하나씩
>
"""

N, Q = map(int, input().split(' '))

road = []
for _ in range(N):
    r = list(map(int, input().split(' ')))
    road.extend(list(range(r[0]+1, r[1])))
    
car = []
for _ in range(Q):
    if int(input()) not in road:
        car.append(road)
        
print(len(car))

"""
2번 문제: 겹치는 사라진 전화번호부
모든 전화번호는 5개 자릿수로 되어있다.
우리는 전화번호부가 있다.
그러나 해당 전화번호부는 낡아서 식별이 안되는 번호들이 있다.
해당 번호들은 ?로 표시

이때, 수신전화에 대하여, 가능한 후보 연락처 이름들을 출력.

- alphabetical order으로 출력
- 없을 시, "NO"

input:

> N개의 연락처와 전화번호, Q개의 수신전화
각 줄에 N개 사람 이름과 번호
각 줄에 Q개 수신전화
>    
"""
N, Q = map(int, input().split(' '))

people = []
for _ in N:
    tst = list(input.split(' '))
    for t in tst:
        if 

num = []
for _ in Q:
    num.append(input())

for n in num:
    for p in people:
        p_list = [i for i, val in enumerate(list(p[1])) if val != '?']
    
    if p_list