# 이진 탐색(Binary Search)

# 배열 내부 데이터가 정렬되어 있을 때만 사용가능
# 무작위일 떄, 사용할 수 없으나 정렬되어 있으면 매우 빠르게 찾을 수 있다.
# 탐색 범위를 절반씩 좁혀 데이터 탐색한다.
# 이진 탐색은 위치를 나타내는 변수 3개를 사용한다.
# 시작점, 끝점, 중간점을 사용한다.
# 목표 데이터와 중간점 데이터를 비교해 찾는 과정

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid =(start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid]==target:
        return mid
    # 중간점 값보다 찾는 값이 작은 경우 왼쪽 배열 확인
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)
# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)