t=int(input())

for _ in range(t):
    total=0
    max_num=0
    num=int(input())
    price=list(map(int,input().split()))

    for i in range(num-1,-1,-1):
        if price[i]>max_num:
            max_num=price[i]
        else:
            total+=(max_num-price[i])
    print(total)