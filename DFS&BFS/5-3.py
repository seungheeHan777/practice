n,m= map(int,input().split())
graph = []
# 얼음 틀에 정보 입력
for i in range(n):
    graph.append(list(map(int, input().split())))
# DFS 메서드 정의
# DFS 함수 정의
def dfs(graph, x,y):
    # 범위에서 벗어나면 바로 종료
    if x<=-1 or x>=n or y <=-1 or y >=m:
        return False
    #  얼음 틀에 얼음이 있을 때
    if graph[x][y]==0:
        # 방문 처리를 한다.
        graph[x][y]=1
        # 상하좌우에 얼음이 있는지를 확인한다.
        dfs(graph, x-1, y)
        dfs(graph, x, y-1)
        dfs(graph, x+1, y)
        dfs(graph, x, y+1)
        # True 호출
        return True
    # 아니면 False 출력
    return False
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
count=0
for i in range(n):
    for j in range(m):
        if dfs(graph,i,j)==True:
            count+=1
print(count)
