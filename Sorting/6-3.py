# 위에서 아래로

# 배열 안의 수를 내림차순으로 정렬
# 첫 줄에 수열애 속해 있는 수의 개수 n 입력 1<=n<=500
# 두번째 줄부터 n+1까지 수 입력(1<=array 값<=100000)

n= int(input())
array=[int(input()) for i in range(n)]
array.sort(reverse=True)
print(array)