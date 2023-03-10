# 구슬 탈출 2
# https://www.acmicpc.net/problem/13460
# 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 
# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 
# 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 
# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
# 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
count=0
dcount=0
# 좌,우 ,상,하 방향
moves=[[-1,0],[1,0],[0,-1],[0,1]]
def find():
    global rx,ry,bx,by,ox,oy
    # R,B,O 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx,ry=i,j
            elif board[i][j] == 'B':
                bx,by=i,j
            elif board[i][j] == 'O':
                ox,oy=i,j

def moving(move_index):
    global char,rx,ry,count,dcount
    char=board[rx+moves[move_index][0]][ry+moves[move_index][1]]
    if char=='O':
            # 문자열 위치 바꾸기
            board[rx][ry]=board[rx+moves[move_index][0]][ry+moves[move_index][1]]
            # R의 좌표 바꾸기
            rx+=moves[move_index][0]
            ry+=moves[move_index][1]
            
            if board[rx][ry]=='O':
                count+=1
                print(count)
    elif char=='.':
        board[rx][ry],board[rx+moves[move_index][0]][ry+moves[move_index][1]]=board[rx+moves[move_index][0]][ry+moves[move_index][1]],board[rx][ry]
        # R의 좌표 바꾸기
        rx+=moves[move_index][0]
        ry+=moves[move_index][1]
        moving(move_index)
        if char=='#':
            count+=1
    elif char=='#':
        rx=rx
        ry=ry
        dcount+=1
while True:
    find()
    # R과 O의 거리 차이
    dx,dy=ox-rx,oy-ry
    
    if count>10:
        print(-1)
        break
    if board[rx][ry]==board[ox][oy]:
        break
    if dx<0:
        move_index=0
        if dcount==2:
            move_index=2
        elif dcount>=3:
            move_index=3
        moving(move_index)
    elif dx>0:
        move_index=1
        if dcount==2:
            move_index=2
        elif dcount>=3:
            move_index=3
        moving(move_index)
    if dy<0:
        move_index=2
        if dcount==2:
            move_index=0
        elif dcount>=3:
            move_index=1
        moving(move_index)
    elif dy>0:
        move_index=3
        if dcount==2:
            move_index=0
        elif dcount>=3:
            move_index=1
        moving(move_index)
    


    
    # for i in range(len(move)):
    #     # 장애물이 있을 때
    #     if board[rx+move[i][0]][ry+move[i][1]]=='#':
    #         board[rx][ry]=board[rx][ry]
    #     # 빈 공간일 때
    #     elif board[rx+move[i][0]][ry+move[i][1]]=='.':
    #         board[rx][ry],board[rx+move[i][0]][ry+move[i][1]]=board[rx+move[i][0]][ry+move[i][1]],board[rx][ry]
    #         count+=1
    #         if count>=10:
    #             print(-1)
    #             break
    #     # 탈출하면 종료
    #     elif board[rx+move[i][0]][ry+move[i][1]]=='O':
    #         board[rx][ry]=board[rx+move[i][0]][ry+move[i][1]]
    #         count+=1
    #         print(count)
    #         break
    #     # 파란 공 제어
    #     if board[bx+move[i][0]][by+move[i][1]]=='O':
    #         board[bx][by]=board[bx][by]
    #     elif board[bx+move[i][0]][by+move[i][1]]=='.':
    #         board[bx][by],board[bx+move[i][0]][by+move[i][1]]=board[bx+move[i][0]][by+move[i][1]],board[bx][by]
