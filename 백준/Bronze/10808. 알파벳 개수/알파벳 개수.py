a=input()
dic=[0]*26

for i in a:
    dic[ord(i)-97]+=1

for j in dic:
    print(j,end=" ")