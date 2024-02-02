T = True

while T:
    st = input()
    if st != '.':
        st = list(st)
        l = []
        for s in st:
            if s == '(' or s == '[':
                l.append(s)
            elif s == ')':
                if len(l) >= 1 and l[-1]=='(':
                    l.pop(-1)
                else:
                    l.append(s)
            elif s == ']':
                if len(l) >= 1 and l[-1]=='[':
                  l.pop(-1)  
                else:
                    l.append(s)
            else:
                pass
        if len(l) == 0:
            print('yes')
        else:
            print('no')
            
    else:
        T = False 