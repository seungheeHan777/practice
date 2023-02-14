# 1로 만들기
# 정수 x가 주어질 때, 
# x에 사용할 수 있는 연산은 4가지이다.
# 1. x가 5로 나누어떨어지면 5로 나눈다.
# 2. x가 3로 나누어떨어지면 3로 나눈다.
# 3. x가 2로 나누어떨어지면 2로 나눈다.
# 4. x에서 1을 뺀다.

# 위의 4가지 연산을 이용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하라.

import sys
# x 값 입력
x=int(sys.stdin.readline())
# arr 리스트를 선언
arr=[0]*(x+1)

# 이 문제를 점화식으로 나타내보자면,
# arr[x]=min(arr[x-1],arr[x//2],arr[x//3],arr[x//5]) 이다
# 이는 다이나믹 프로그래밍에서 Bottom-Up 방식을 이용해 구현하면
# 반복문을 사용해서 arr[i]에 값을 저장해서 점점 x에 다가가는 방식이다.
for i in range(2,x+1):
    arr[i]=arr[i-1]+1
    if i%2==0:
        arr[i]=min(arr[i],arr[i//2]+1)
    if i%3==0:
        arr[i]=min(arr[i],arr[i//3]+1)
    if i%5==0:
        arr[i]=min(arr[i],arr[i//5]+1)
print(arr[x])