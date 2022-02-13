# 문제
# 행과 열을 입력받고
# 0 과 1로 이루어진 2차원 배열을 입력받는다
# 0은 벽이고 1은 길이다
# 제일왼쪽 맨위에서 출발해서 제일 오른쪽 맨아래가 출구이다.
# 나갈수있는 길은 항상 있다.
# 이떄 나가는 최단경로를 추력하는 프로그램을 작성한다.
# 
# 입력조건
# 젓째줄에 두정수 N,M (4<= N,M <= 200) 이 주어진다. 다음 N개의 줄에서 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백ㅇ벗이 붙어서 입력으로 제시된다.
# 또한 시작칸과 마지막칸은 항상 1이다. 
#
# 출력조건 
# 첫째줄에 최소 이동칸의 개수를 출력한다.

# BFS 공유 경로그랲을 활용한 풀이이다. (당연 풀이는 많겠지)


from collections import deque

# N,M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌떄까지 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))