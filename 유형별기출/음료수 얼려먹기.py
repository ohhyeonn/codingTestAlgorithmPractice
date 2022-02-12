# 문제
# 행과 열을 입력받고
# 0 과 1로 이루어진 2차원 배열을 입력받는다
# 이떄 서로 부터있는 0 끼리는 count 를 하나로 쳐준다 
# 2차월 배열의 서로붙어있는 0 으로 이루어진 그룹의 개수를 출력 하는 프로그램을 작성한다.
# 
# 
# 입력조건
# 첫 번째 줄에 얼음 틀의 세로 길이N과 가로길이 M이 주어진다. (1 <= N, M <= 1000)
# 두번째 줄부터 N + 1 번째 줄까지얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0 그렇지 않은 부분은 1이다.
# 
# 출력조건 
# 한번에 만들수 있는 아이스크림의 개수를 출력한다. 

# DFS 로 하나의 구멍을 만났을때 근처의 모든 구멍까지 찾아서 함께 막는 식으로 DFS로 한그룹을 막을때 카운트 하나를 늘리는 식으로 풀이를 할수 있다.



# N,M 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 2차월 리스트의 맵 정보를 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나느 경우에는 즉시 종료
    if x <= -1 or x>=n or y<= -1 or y>= m:
        return False
    # 현제 노드를 아직 망문하지 않았다면
    if graph[x][y]  == 0:
        # 해당 노드를 방문처리
        graph[x][y] = 1
        # 상 하 좌 우 위치도 모두 재귀적으로 호출
        dfs(x -1 , y)
        dfs(x ,y-1)
        dfs(x+1 ,y)
        dfs(x , y+1)
        
        # 처음 방문하는 경우라면 True 리턴
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 호출 return 값으로 count를 센다
        if dfs(i,j) == True:
            result += 1

# 정답 출력
print(result) 
