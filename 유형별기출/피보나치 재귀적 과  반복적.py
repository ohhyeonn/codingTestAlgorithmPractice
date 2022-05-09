

# 재귀적!!!!!!
# 한 번 계산된결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100
# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2 일떄 1을 반환)
    if x== 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 무제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x -2)
    return d[x]

print(fibo(99))







# 반복적!!!!!!!
# 앞서 계산된 결과를 저장ㅈ하기 위한 DP테이블 초기화
d = [0] * 100
# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99
# 피보나치 함수(Fibonacci Function)반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i -1] +d[i -2]

print(d[n])