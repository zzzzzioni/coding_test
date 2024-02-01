# 미해결 

S = []
T = True

while T:
    s = input()
    if s != '.':
        S.append(s)
    else:
        T = False 
    
for i in range(len(S)):

    s = list(S[i])
    
    if s.count('(') == s.count(')') and s.count('[') == s.count(']'):
        pass
        if s.count('(') == 0:
            print('yes')
        else:
            pass
    else:
        print('no')

    
        
