a=list(input())
chk1=0
chk2=0

if int(a[0])==0:
    chk1+=1
elif int(a[0])==1:
    chk2+=1

for i in range(len(a)-1):
    if int(a[i])==0:
        if a[i]!=a[i+1]:
            chk2+=1

    elif int(a[i])==1:
        if a[i]!=a[i+1]:
            chk1+=1

if chk1>=chk2:
    print(chk2)
else:
    print(chk1)