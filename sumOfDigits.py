i=int(input())
x=0
j=1
while(j<i):
    x+=int(i/j%10)
    j*=10
print(x)