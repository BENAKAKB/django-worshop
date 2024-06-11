def perm3(c):
   
    c1=c[0:1]
    c2=c[1:2]
    c3=c[2:3]
    list3=[]
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c2+c1)
    list3.append(c3+c1+c2)
    return list3

def per4(st):
    c1=st[0:1]
   
    l= perm3(st[1:])
    for i in l:
        print(c1+i)
       
    c2=st[1:2]  
    l= perm3(st[2:]+c1)
    for i in l:
        print(c2+i)    
   
    c3=st[2:3]
    l= perm3(st[3:]+c1+c2)
    for i in l:
        print(c3+i)
    c4=st[3:4]
    l= perm3(c1+c2+c3)
    for i in l:
        print(c4+i)
per4('fast')