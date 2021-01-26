with open ('lista clasei.txt' ,'r') as f:
    x=list(eval(f.readline()))
x.sort()
with open ('lista clasei.2.txt','w') as f:
   for i in range(0,len(x)):
        f.write(str(x[i]))
        f.write('\n')
   
