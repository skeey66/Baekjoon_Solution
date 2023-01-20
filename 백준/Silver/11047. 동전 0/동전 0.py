num, money=map(int,input().split())
coin=[]
count=0

for i in range(num):
    coin.append(int(input()))

for j in range(num-1,-1,-1):
    count+=(money//coin[j])
    money%=coin[j]

print(count)