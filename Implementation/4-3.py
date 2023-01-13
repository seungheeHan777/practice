# 4-3 왕실의 나이트
# 8*8 좌표평면이 있다. 나이트는 이 위에서 이동하는데 이 때, 나이트는 이 밖을 넘어갈 수 없다.
# 나이트는 L자로만 이동이 가능하며 2가지 경우로 이동한다.
# 1. 수평으로 두 칸 이동 후, 수직으로 한 칸 이동하는 경우
# 2. 수직으로 두 칸 이동 후, 수평으로 한 칸 이동하는 경우
# 행의 위치는 1-8, 열의 위치를 a-h로 표현한다.
# 이 때, 나이트의 위치를 입력받고, 나이트가 좌표평면 위에서 이동하는 경우의 수를 구하라.

knight=input()
x=knight[0:1]
x=ord(x)-ord('a')+1 # 문자를 숫자로 변환하기 위해서 ord이용, a를 1로 기준으로 계산
y=int(knight[1:])
move_case=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count=0 # 경우의 수
for i in move_case:
    if 0<x-i[0]<=8:
        if 0<y-i[1]<=8:
            count+=1
print(count)

# 답안
# knight=input()
# x=knight[0:1]
# x=ord(x)-ord('a')+1 # 문자를 숫자로 변환하기 위해서 ord이용, a를 1로 기준으로 계산
# y=int(knight[1:])
# steps=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
# count=0
# for step in steps:
#     next_y=y+step[1]
#     next_x=x+step[0]
#     if 1<=next_x<=8 and 1<=next_y<=8:
#         count+=1
# print(count)