# 바닥 공사
# 가로 n, 세로 2 직사각형 의 바닥이 있다
# 이를 1*2,2*1,2*2 덮개를 이용해서 채우고자 한다.
# 이 때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성
# 입력 조건: n 입력
# 출력 조건: 모든 경우의 수를 796,796로 나눈 나머지를 출력

# 이 문제를 다이나믹 프로그래밍으로 풀어보려면
# 먼저 점화식을 구해야 한다.
# n 이 있을 때, n을 분리해서 구해야 하는데
# 이 때, 1짜리 타일로 나눌지 2짜리 타일로 나눌지를 결정해야한다.
# 이 때 n-2와 2짜리 타일에서 2짜리 타일은 두 가지로 나눌 수 있다.
# 따라서 점화식을 구해보면
# f(n)=f(n-1)*1+f(n-2)*2 이다.

import sys
n=int(sys.stdin.readline())
def f(k):       # Top-Dowm
    if k == 1:
        return 1
    elif k == 2:
        return 3
    else :
        return f(k-1)+f(k-2)*2
# print(f(n)%796796)

a=[0]*n
for i in range(n):      # Bottom Up
    if i == 0:
        a[i]=1
    elif i == 1:
        a[i]=3
    else:
        a[i]=a[i-1]+a[i-2]*2
a[n-1]%=796796
print(a[n-1])