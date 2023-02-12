# 부품 찾기를 계수 정렬을 이용해서 풀기
# 계수 정렬 : 정수형 데이터를 다룰 때, 모든 범위를 담는 크기의 리스트를 선언
import sys
n=int(sys.stdin.readline().rstrip())
array=[0]*1000001

for i in sys.stdin.readline().rstrip().split():
    array[int(i)]=1
m=int(sys.stdin.readline().rstrip())
array2=list(map(int,sys.stdin.readline().split()))
for i in array2:
    if array[i]==1:
        print("yes",end=' ')
    else:
        print("no",end=' ')
