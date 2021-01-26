with open ('lista clasei.txt' ,'r') as f:
    x=list(eval(f.readline()))
x.sort()
v=''
i=str
while i!='SFARSIT':
    for i in x:
        v=v+str(i)
        v=v+str(' ')
        with open ('lista clasei.2.txt','w') as f:
            f.write(v)
            f.write('\n')
    else :
        break
        
