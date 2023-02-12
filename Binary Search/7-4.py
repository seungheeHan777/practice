# 떡볶이 떡 만들기
# 떡의 길이가 일정하지 않아 절단기로 잘라서 맞춰야한다.
# 절단기에 높이 h를 지정하면 줄지어진 떡을 한 번에 절단한다.
# h보다 긴 떡은 h 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.
# ex) 19,14,10,17 cm 떡이 있고, 높이를 15로 지정하면
# 15,14,10,15 가 된다. 잘린 떡은 4  0 0 2 이다.
# 손님은 6 만큼의 길이를 가져간다.
# 손님이 왔을 때, 총 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하라

# 입력 조건: 첫 줄에 떡의 개수 n, 요청한 떡의 길이m 
# 두번째 줄에 떡의 개별 높이가 주어짐. 높이의 총합은 항상 m이상이고
# 손님은 필요한 양만큼 사갈 수 있다.
# 출력 조건: 적어도 m만큼의 떡을 집에 가져가기 위해 
# 절단기에 설정할 수 있는 높이의 최댓값을 출력

import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
max=0
def binary_search(start,end,array):
    global max
    sum=0
    mid=(start+end)//2
    h=array[mid]
    for i in array:
        if (i-h)>0:
            sum+=i-h
            # m을 충족시킬 떄
    if sum >=m:
        # max가 바뀔 때
        if max<h:
            max=h
            binary_search(mid+1,end,array)
    else:
        binary_search(start,mid-1,array)
    return max
print(binary_search(0,len(arr)-1,arr))
# max=0
# arr.sort()
# for h in range(arr[0]):
#     sum=0
#     for i in arr:
#         if (i-h)>0:
#             sum+=i-h
#             if sum >=m:
#                 if max<h:
#                     max=h
# print(max)