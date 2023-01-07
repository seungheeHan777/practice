
# 3-2 큰 수의 법칙
# 다양햔 수로 이루어진 배열이 있을 때 주어진 수를 m번 더해 가장 큰 수를 만들어야 한다.
# 이 때, 특정 인덱스가 연속해서 k번을 초과하면 안된다.

# n=int(input(" 배열의 개수 입력 (2<=n<=1000): "))
# m=int(input(" 더하기를 몇 번 할 지 입력 : (1<=n<=10000): "))
# k=int(input(" 최대로 더할 수 있는 숫자 : (1<=n<=10000): "))

n,m,k = map(int,input().split())
number = list(map(int,input().split()))
# i=0
# for i in number :
#     if first<=i:  # 가장 큰 수와 배열을 비교한다
#         if second==0 :  # 처음에 배열을 비교할 때 0이 초기값이므로 number[0]을 대입한다.
#             second=i
#             first=i
#         else :  # 처음에 비교하는 것 말고 이외에 배열을 비교할 때
#             second = first
#             first = i
#     elif first==second:   # 2번쨰로 배열을 비교할 때는 가장 큰 수와 두 번쨰로 큰 수에 같은 수가 들어간다 이 경우에는 first > number 이므로 두번째로 큰 수에 number를 삽입한다.
#         second=i
number.sort()
first=number[n-1]
second=number[n-2]
quotient = m//(k+1) # 몫
remainder = m%(k+1) # 나머지
# 계산에서 나오는 큰 수는 first를 k번 더하고, second 를 한 번 더한 것을 반복하는 것이다. first*k+second이다.
# 따라서 이를 계산하는 식은 m을 k+1로 나눈 몫을 first*k+second과 곱한 것과 m을 k+1로 나눈 나머지를 first를 곱한 것을 더한 것이다.
# quotient*(first*k+second)+first*remainder
max=quotient*(first*k+second)+first*remainder

print(max)