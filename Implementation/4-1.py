n= int(input())
plan=list(map(str,input().split()))
x=1
y=1
for i in plan:
    if i=='u':
        if x==1:
            x=x
        else:
            x-=1
    elif i =='d':
        if x==n:
            x=x
        else:
            x+=1
    elif i =='l':
        if y==1:
            y=y
        else:
            y-=1
    elif i =='r':
        if y==n:
            y=y
        else:
            y+=1
print(x , y)