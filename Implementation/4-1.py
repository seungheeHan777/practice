#상하죄우 문제
# n,n 정사각형이 있고 1,1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽위 좌표가 1,1, 가장 오른쪽 아래 좌표는 n,n이다.
# a가 이 위를 이동한다고 할 때, 왼쪽, 오른쪽, 위 , 아래 방향으로만 움직일 수 있다.
# 단, 이때 n,n 크기의 정사각형 공간을 벗어나는 움직임은 무시한다.
# 최종적으로 a가 도착하는 좌표를 구하라.

# 내가 푼 답
# n= int(input())
# plan=list(map(str,input().split()))
# x=1
# y=1
# for i in plan:
#     if i=='u':
#         if x==1:
#             x=x
#         else:
#             x-=1
#     elif i =='d':
#         if x==n:
#             x=x
#         else:
#             x+=1
#     elif i =='l':
#         if y==1:
#             y=y
#         else:
#             y-=1
#     elif i =='r':
#         if y==n:
#             y=y
#         else:
#             y+=1
# print(x , y)

# 답지
n= int(input())
plans=input().split()
x,y=1,1
# dx[i],dy[i] 를 묶어서 계산하면 u,d,l,r 의 방향계산가능
dx=[0,0,-1,1]
dy=[-1,1,0,0]
# 방향
move_types=['l','r','u','d']
# 입력한 값 순서대로 방향 계산
for plan in plans:
    # len(move_types)==4 이므로 0-3까지 대입해서 반복해서 plan에 해당하는 방향과 맞으면 실행
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx= x+dx[i]
            ny= y+dy[i]
    #예외 일때,
    if nx<1 or ny<1 or nx>n or ny >n:
        continue
    x,y=nx,ny
print(x,y,len(move_types))