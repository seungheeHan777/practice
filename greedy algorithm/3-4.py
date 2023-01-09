n,k=map(int,input().split())
count=0
while n!=1:
    if n%k ==0:
        n/=k
        count+=1
    else:
        n-=1
        count+=1
print(count)

# 풀이 답안

# 일단 n을 k로 나누는 과정이 많이 반복될수록 빠르게 n==1로 만들 수 있다.
# 따라서 n이 k로 나누어 떨어질 때는 그냥 -1을 하지말고 k로 나눠야한다.

# n,k=map(int,input().split())
# result=0
# while n>=k:
#     #n이 k로 나누어 떨어지지 않는다면 -1 한다.
#     while n%k !=0:
#         n-=1
#         result+=1
#     n//=k
#     result+=1

# # n의 값이 k보다 작아질 경우에는 나눌 수 없으므로 1이 될 때까지 -1을 해준다.
# while n>1:
#     n-=1
#     result+=1

# print(result)