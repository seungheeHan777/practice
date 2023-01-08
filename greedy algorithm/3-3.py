n,m=map(int,input("행, 열 입력: ").split())
number = [0 for i in range(n)]
small=[] # 각 행에서 가장 작은 값을 저장하는 리스트
for i in range(n):
    number[i] = list(map(int,input().split())) # 각 행마다 값을 저장
    number[i].sort()    # i번째 행에서 내립차순으로 정렬
    small.append(number[i][0]) # 각 행에서 가장 작은 값 저장
# number[0].sort()    #오름차순으로 정렬 [0]이 가장 작은 값
small.sort(reverse=True)    #small 리스트를 내림차순으로 정렬해서 small[0]에 가장 큰 값이 오도록해서 정답이 되도록 유도
print(number)
print(small)
print(small[0]) # 정답 출력