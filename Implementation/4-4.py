# 4-4 게임 개발
# 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 할 떄, 1*1 크기의 정사각형으로 이뤄진 n*m 크기의 직사각형으로 육지 또는 바다이다
# 캐릭터는 동서남북 중 한 곳을 바라본다.
# (a,b)로 나타내고, a는 북쪽으로 떨어진 칸의 개수 ,b는 서쪽으로 떨어진 땅의 개수이다.
# 메뉴얼은 다음과 같다.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽(반시계)부터 차례대로 갈 곳을 정함
# 2. 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 있다면, 왼쪽으로 회전 후 전진한다. 왼쪽에 없다면 왼쪽 방향으로 회전만 하고 1단계로 돌아간다.
# 3. 네 방향 모두 이미 가보거나 바다라면, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 이 때, 뒤쪽이 바다라면 움직임을 멈춘다.
# def left():
#     global a,b,d,direction_count,count
#     while True:
#         # 1단계
#         d-=1
#         if d==-1:
#             d=3
#         # 방향 확인
#         # 2단계
#         # 북쪽일 때
#         if d==0:
#             # 방향이 북쪽일 때, if문으로 앞으로 이동할 곳이 바다인지 육지인지 확인
#             if coordinate[a][b+1]==0:
#                 coordinate[a][b]=1
#                 b+=1
#                 count+=1
#                 # 이동하면 0으로 바꿔서 못 움직이게 한다.
#                 direction_count =0
#             # 바다일 경우, direction_count 변수에 1을 더한다.
#             else :
#                 direction_count+=1
#             # 방향이 동쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
#         elif d==1:
#             if coordinate[a+1][b]==0:
#                 coordinate[a][b]=1
#                 a+=1
#                 count+=1
#                 coordinate[a+1][b]=1
#                 direction_count =0
#                 # 바다일 경우, direction_count 변수에 1을 더한다.
#             else :
#                 direction_count+=1
#         # 방향이 남쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
#         elif d==2:
#             if coordinate[a][b-1]==0:
#                 coordinate[a][b]=1
#                 b-=1
#                 count+=1
#                 coordinate[a][b-1]=1
#                 direction_count =0
#                 # 바다일 경우, direction_count 변수에 1을 더한다.
#             else :
#                 direction_count+=1
#         # 방향이 서쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
#         elif d==3:
#             if coordinate[a-1][b]==0:
#                 coordinate[a][b]=1
#                 a-=1
#                 count+=1
#                 coordinate[a-1][b]=1
#                 direction_count =0
#                 # 바다일 경우, direction_count 변수에 1을 더한다.
#             else :
#                 direction_count+=1

#         if direction_count == 4:
#             # 방향에 따라 뒤로 가는 곳이 달라지므로 if 문으로 경우의 수를 확인한다.
#             if d==0:
#                 # 방향이 북쪽일 때, if문으로 앞으로 이동할 곳이 바다인지 육지인지 확인
#                 if coordinate[a][b-1]==0:
#                     b-=1
#                     direction_count =0
#                 else :
#                     break
#                 # 방향이 동쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
#             elif d==1:
#                 if coordinate[a-1][b]==0:
#                     a-=1
#                     direction_count =0
#                 else :
#                     break
#             # 방향이 남쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
#             elif d==2:
#                 if coordinate[a][b+1]==0:
#                     b+=1
#                     direction_count =0
#                 else :
#                     break
#             # 방향이 서쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
#             elif d==3:
#                 if coordinate[a+1][b]==0:
#                     a+=1
#                     direction_count =0
#                 else :
#                     break

        
# n,m=map(int,input().split())    # n,m 공백으로 입력 맵의 크기설정
# a,b,d=map(int,input().split())  # a,b,n 공백으로 입력 a,b는 캐릭터의 좌표,d는 방향으로 0:북,1:동,2:남,3:서
# coordinate=[0 for i in range(n)]    # n만큼 선언
# direction_count=0 # 3단계에서 확인하기 위한 direction_count 변수 4가 되면 3단계 실행
# # 처음에 있는 위치 포함
# count=1
# # 좌표에 육지와 바다 구분
# for i in range(n):
#     coordinate[i]=list(map(int,input().split()))

# left()
# print(count)

# 답안
# d[][]로 방문한 위치를 저장하고, array[][]로 전체 맵의 정보를 저장해서 둘을 따로 표기
# 그 다음에 조건문에서 and 로 방문하지 않고 땅인 부분을 모두 만족시키는지 확인
# dx 와 dy로 동,서,남,북 일 때 움직여야 하는 좌표를 계산
# 중간 중간에 direction 과 turn_time 으로 방향 설정과 방향을 몇 번 바꿨는지 확인해서 탈출문 작성
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)