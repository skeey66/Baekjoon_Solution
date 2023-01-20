num=int(input())
P=[]
sum=0
v=0

P=list(map(int,input().split()))

P=sorted(P)

for i in P:
    v+=i
    sum+=v
    
print(sum)