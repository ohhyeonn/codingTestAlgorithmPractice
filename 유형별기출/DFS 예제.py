# DFS 메서드 정의

# 그래프와 한노드의키를 받는다 그래서 그노드방문처리하고 그노드의인접에방문안한거있으면 그노드다시재귀호출한다 (재귀 호출할때 포문으로 돌리는데 작은순에대한 로직은 없다 걍 포문으로 오는 순서대로 방문하게된다)
def dfs(graph , v, visited):
    # 현재노드를 방문 처리
    visited[v] = True
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph , i , visited)

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

dfs(graph, 1, visited)