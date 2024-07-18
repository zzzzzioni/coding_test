N = int(input())
S = list(map(int, input().split(' ')))
M = int(input())
C = list(map(int, input().split(' ')))

#################################################
#   오늘의 배움 : Dictionary의 in 연산은 O(1)이다.    #
# 반면 list의 in 연산이나 indexing, count는 O(N)이다. #
#        Set의 in 연산 시간복잡도도 O(1)이다          #
#################################################


### 딕셔너리로 풀기는 완료 
D = {}
for c in C:
    D[c] = 0


for s in S:
    if s in D:
        D[s] += 1
        
for c in C:
    print(D[c], end=' ')


### 하씨 ... binary search로 어케 푸는 것임 ㅠㅠ

# C.sort()

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2
    
#     if array[mid] == target:
#         D[target] += 1
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)

# for s in S:
#     binary_search(C, s, 0, M-1)
    
# print(* D.values())
    
