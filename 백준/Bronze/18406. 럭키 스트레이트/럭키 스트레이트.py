import sys
a=sys.stdin.readline().rstrip()
chk1=0
chk2=0
length=len(a)
for i in range(length//2):
    chk1+=int(a[i])

for i in range(length//2,length):
    chk2+=int(a[i])

if chk1==chk2:
    print("LUCKY")
else:
    print("READY")