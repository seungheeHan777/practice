# 부품 찾기
# 전자 매장에 부품이 n개 있다.
# 각 부품은 정수 형태의 고유 번호가 있다.
# 어느 날 손님이 m개 종류의 부품을 대량으로 구매해 견적서를 요청
# 주인은 문의한 부품 m개 종류를 모두 확인해 견적서를 작성
# 이떄 가게 안에 부품이 모두 있는지 확인하는 프로그램 작성.

# 입력 조건: 첫째 줄에 n 1~1,000,000
# 둘쨰 줄에 공백으로 n개의 정수
# 셋째 줄에 정수 m
# 넷째 줄에 공백으로 구분해 m개 주어짐. 1~1,000,000
# 출력 조건: 첫째 줄에 공백으로 구분해 각 부품이 존재하면 yes, 없으면 no

# 이진 탐색을 이용한 답안
# 최악의 경우 시간 복잡도는 O(M * lon n)
# 결과적으로 이진 탐색을 사용하는 문제 풀이 방법의 경우
# 시간 복잡도는 O((m+n)*lon n) 이다.
import sys
def binary_search(arr,target,start,end):
    if start> end:
        return None
    mid= (start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

n=int(sys.stdin.readline().rstrip())
array1=list(map(int,sys.stdin.readline().split()))
array1.sort()
m=int(sys.stdin.readline().rstrip())
array2=list(map(int,sys.stdin.readline().split()))
for i in range(m):
    result=binary_search(array1,array2[i],0,n-1)
    if result==None:
        print("no",end=' ')
    else:
        print("yes",end=' ')

