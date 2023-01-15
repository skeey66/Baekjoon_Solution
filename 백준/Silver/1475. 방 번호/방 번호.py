a=int(input())
b=list(str(a))
c=list()
max=0

for i in range(10):
    c.append(b.count(str(i)))

if (int(c[6])+int(c[9]))%2 == 0:
    d=(int(c[6])+int(c[9]))/2
else:
    d=(int(c[6])+int(c[9]))/2+1

c[6]=int(d)
c[9]=int(d)
for i in c:
    if max<int(i):
        max=int(i)

print(max)