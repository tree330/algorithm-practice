a= int(input()) ; b=int(input()) ; c=int(input())
t=str(a*b*c)
for i in range(0,10):
    print(t.count(str(i)))
