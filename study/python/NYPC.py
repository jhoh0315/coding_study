N=int(input())
a=[]
for i in range(N):
    a.append(input())


n=int(input())

for i in range(n):
    b=input()
    if b in a:
        a.remove(b)
        N-=1

print(N)
print(a)
for i in range(N):
    print(a[i])
