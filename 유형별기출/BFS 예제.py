# BFS

# DFS 에서는 재귀로했는데 아래와같이 DFS도 stack을 이용한 while로 구현 가능하다

from collections import deque
# 그래프와 한노드의키를 받는다 그래서 그노드방문처리하고 그노드의인접에방문안한거있으면 그노드 큐에 넣는다.
def bfs(graph , v, visited):
    # 큐(Queue) 구현을 위해 depue 라이브러리 사용
    queue = deque([v])
    # 현재 노드를 방문처리
    visited[v] = True
    # 큐가  빌때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력
        node = queue.popleft()
        print(node, end=' ')
        # 해당 원소의 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 인접리스트 그래프 선언 (각 노드가 연결된 정보를 리스트 자료형으로 표현)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False]*9

bfs(graph, 1, visited)