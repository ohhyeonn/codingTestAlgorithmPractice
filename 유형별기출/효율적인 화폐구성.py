# 문제
# 
# 입력조건
# 첫째 줄에 N,M이 주어진다. (1<=N<= 100 , 1<=M<=10000)
# 이후N개의줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10000보다 작거나 같은 자연수 이다.
# 
# 출력조건 
# 첫째줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
# 불가능할 때는 -1을 출력한다.



# 정수 N,M을 입력받기
n,m = map(int , input().split())
# N개의 화폐단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))
# 한번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)
#다이나믹 프로그래밍 진행 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i] , m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j] , d[j-array[i]]+1)
# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else :
    print(d[m])