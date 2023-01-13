n,m=map(int,input().split())    # n,m 공백으로 입력 맵의 크기설정
a,b,d=map(int,input().split())  # a,b,n 공백으로 입력 a,b는 캐릭터의 좌표,d는 방향으로 0:북,1:동,2:남,3:서
coordinate=[0 for i in range(n)]    # n만큼 선언
# 좌표에 육지와 바다 구분
for i in range(n):
    coordinate[i]=input().split()
print(coordinate)