n=int(input(" 배열의 개수 입력 (2<=n<=1000): "))
m=int(input(" 더하기를 몇 번 할 지 입력 : (1<=n<=10000): "))
k=int(input(" 최대로 더할 수 있는 숫자 : (1<=n<=10000): "))

number = list(map(int,input().split()))
big=0
second=0
i=0
for i in number :
    if big<=i:  # 가장 큰 수와 배열을 비교한다
        if second==0 :  # 처음에 배열을 비교할 때 0이 초기값이므로 number[0]을 대입한다.
            second=i
            big=i
        else :  # 처음에 비교하는 것 말고 이외에 배열을 비교할 때
            second = big
            big = i
    elif big==second:   # 2번쨰로 배열을 비교할 때는 가장 큰 수와 두 번쨰로 큰 수에 같은 수가 들어간다 이 경우에는 big > number 이므로 두번째로 큰 수에 number를 삽입한다.
        second=i
quotient = m//(k+1)
remainder = m%(k+1)
max=quotient*(big*k+second)+big*remainder


print(max)