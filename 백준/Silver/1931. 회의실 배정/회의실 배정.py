num=int(input())
time=[]

for _ in range(num):
    s,e=map(int,input().split())
    time.append([s,e])

time=sorted(time,key=lambda a:a[0])
time=sorted(time,key=lambda a:a[1])

fin=0
count=0

for s,e in time:
    if s>=fin:
        fin=e
        count+=1
print(count)