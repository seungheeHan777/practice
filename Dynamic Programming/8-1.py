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
x=int(sys.stdin.readline())
def a():
    global x,count
    x/=5
    count+=1
def b():
    global x,count
    x/=3
    count+=1
def c():
    global x,count
    x/=2
    count+=1
def d():
    global x,count
    x-=1
    count+=1
count=0
while x>1:
    if x%5==0:
        a()
    elif x%3==0:
        b()
    elif x%2==0:
        c()
    else :
        d()
print(count)