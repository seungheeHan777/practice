# 5-4 미로 탈출

# n*m 크기의 직사각형 미로가 있다. 이 때, 시작점은 (1,1)이고, 출구는 (n,m)이다.
# 미로는 한 칸씩 이동가능하며, 괴물이 있는 곳은 이동할 수 없다. 이 때, 탈출하기 위한 최소 칸의 개수를 구하라.
# 괴물이 있는 곳은 0, 괴물이 없는 곳은 1로 표기한다.

# 이 문제는 BFS를 이용해서 풀어야 한다. 통과할 수 있는 노드를 지날 때마다 그 이전 노드의 값에 1을 더해 리스트에 저장해서 마지막 좌표에 도달했을 때, 
# 값을 출력하면 최솟값이 나온다. 
# 이 때, 다시 되돌아가는 일을 방지하기 위해서 1일떄를 우선적으로 탐색한다.

from collections import deque

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y):
    # 큐에 시작노드 삽입
    queue = deque()
    queue.append((x,y))
    # 이동횟수 1 증가

    while queue:
        x,y=queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            # 미로를 넘어가면 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 괴물이 있을 때 제외
            if graph[nx][ny] ==0:
                continue
            # 처음 방문할 때만 기록해야 최단 거리를 기록한다.
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]

# bfs 로 결과 출력
print(bfs(arr,0,0))