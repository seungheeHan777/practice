# 3-3 숫자 카드 게임
# 1. 숫자가 쓰인 카드가 n*m 형태로 놓여있다. n은 행의개수 m은 열의 개수이다. 
# 2. 먼저 뽑을려고 하는 카드의 행을 선택한다
# 3. 그 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 행을 선택할 때, 해당 행에서 가장 숫자가 낮은  카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

n,m=map(int,input("행, 열 입력: ").split())
number = [0 for i in range(n)]
small=[] # 각 행에서 가장 작은 값을 저장하는 리스트
for i in range(n):
    number[i] = list(map(int,input().split())) # 각 행마다 값을 저장
    number[i].sort()    # i번째 행에서 내립차순으로 정렬
    small.append(number[i][0]) # 각 행에서 가장 작은 값 저장
small.sort(reverse=True)    #small 리스트를 내림차순으로 정렬해서 small[0]에 가장 큰 값이 오도록해서 정답이 되도록 유도
print(number)
print(small)
print(small[0]) # 정답 출력

# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것

# 다른 답안
# result =0
# for i in range(n):
#     number =list(map(int,input().split()))
#     min_value =min(number)
#     result=max(result,min_value)