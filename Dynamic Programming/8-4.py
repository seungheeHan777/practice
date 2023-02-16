# 효율적인 화폐 구성

# n가지 종류의 화폐가 있다.
# 이 개수를 최소한으로 이용해서 그 가치의 합이 m원이 되도록 하려고 한다.
# 각 화폐는 몇 개라도 사용할 수 있다.
# 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분.
# 입력 조건: 첫 줄에 n,m이 주어짐
# 이후 n개의 줄에는 각 화폐의 가치가 주어짐. 화폐 가치는 10,000이이다.
# 출력 조건: 첫 줄에 m원을 만들기 위한 최소 화폐 개수 출력
# 불가능 할 때는 -1을 출력
import sys
n,m=map(int,sys.stdin.readline().split())
money=[]
# 테이블 초기화
case=[10001]*(m+1)
for i in range(n):
    money.append(int(sys.stdin.readline()))
money.sort()
case[0]=0
# Bottom Up 
# 점화식은 a[i]=min(a[i],a[i-k]+1)
for i in range(money[0],m+1):
    for j in money:
        if case[i-j]!=10001:    # i-k원을 만드는 방법이 존재하는 경우
            case[i]=min(case[i],case[i-j]+1)
if case[m]==10001:
    print(-1)
else:
    print(case[m])