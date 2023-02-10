# 순차 탐색(Sequential Search)
# 리스트 안에 특정 data를 찾기 위해 
# 앞에서부터 data를 하나씩 순차적으로 확인하는 방법
# 시간만 충분하면 항상 찾을 수 있다.
# 말그대로 순차적으로 리스트안에 데이터를 처음부터 찾는 것이다.
# 순차탐색은 데이터의 정렬 여부와 관계없이 하나씩 확인한다.
# 따라서 데이터의 크기가 n개일 때 n번 비교하므로
# 최악의 시간 복잡도는 O(n)이다.

# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
    return -1 # 원소를 찾지 못한 경우 -1 반환

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열
print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")  
array = input().split()
# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))