def left():
    global a,b,d,direction_count,count
    while True:
        # 1단계
        d-=1
        if d==-1:
            d=3
        # 방향 확인
        # 2단계
        # 북쪽일 때
        if d==0:
            # 방향이 북쪽일 때, if문으로 앞으로 이동할 곳이 바다인지 육지인지 확인
            if coordinate[a][b+1]==0:
                coordinate[a][b]=1
                b+=1
                count+=1
                # 이동하면 0으로 바꿔서 못 움직이게 한다.
                direction_count =0
            # 바다일 경우, direction_count 변수에 1을 더한다.
            else :
                direction_count+=1
            # 방향이 동쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
        elif d==1:
            if coordinate[a+1][b]==0:
                coordinate[a][b]=1
                a+=1
                count+=1
                coordinate[a+1][b]=1
                direction_count =0
                # 바다일 경우, direction_count 변수에 1을 더한다.
            else :
                direction_count+=1
        # 방향이 남쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
        elif d==2:
            if coordinate[a][b-1]==0:
                coordinate[a][b]=1
                b-=1
                count+=1
                coordinate[a][b-1]=1
                direction_count =0
                # 바다일 경우, direction_count 변수에 1을 더한다.
            else :
                direction_count+=1
        # 방향이 서쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
        elif d==3:
            if coordinate[a-1][b]==0:
                coordinate[a][b]=1
                a-=1
                count+=1
                coordinate[a-1][b]=1
                direction_count =0
                # 바다일 경우, direction_count 변수에 1을 더한다.
            else :
                direction_count+=1

        if direction_count == 4:
            # 방향에 따라 뒤로 가는 곳이 달라지므로 if 문으로 경우의 수를 확인한다.
            if d==0:
                # 방향이 북쪽일 때, if문으로 앞으로 이동할 곳이 바다인지 육지인지 확인
                if coordinate[a][b-1]==0:
                    b-=1
                    direction_count =0
                else :
                    break
                # 방향이 동쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
            elif d==1:
                if coordinate[a-1][b]==0:
                    a-=1
                    direction_count =0
                else :
                    break
            # 방향이 남쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
            elif d==2:
                if coordinate[a][b+1]==0:
                    b+=1
                    direction_count =0
                else :
                    break
            # 방향이 서쪽일 때, 앞으로 이동할 곳이 바다인지 육지인지 확인
            elif d==3:
                if coordinate[a+1][b]==0:
                    a+=1
                    direction_count =0
                else :
                    break

        
n,m=map(int,input().split())    # n,m 공백으로 입력 맵의 크기설정
a,b,d=map(int,input().split())  # a,b,n 공백으로 입력 a,b는 캐릭터의 좌표,d는 방향으로 0:북,1:동,2:남,3:서
coordinate=[0 for i in range(n)]    # n만큼 선언
direction_count=0 # 3단계에서 확인하기 위한 direction_count 변수 4가 되면 3단계 실행
# 처음에 있는 위치 포함
count=1
# 좌표에 육지와 바다 구분
for i in range(n):
    coordinate[i]=list(map(int,input().split()))

left()
print(count)