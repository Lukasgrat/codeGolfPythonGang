x=int(input())
s=""
for j in range(x):
    i=0
    t=""
    while(i<j):
        i+=1
        t+="*"
    s+=t
    s+="\n"
s+= t+"*"+s[::-1]
print(s)