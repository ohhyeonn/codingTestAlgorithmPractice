# 문제
# 개미가 식량을 터는 메꺼니즘 
# 개미가 들키지 않기위해서는 최소한 한칸 이상 떨어진 식량 창고를 약탈해야 한다.
#
# 첫번째 줄에 식량차고의 개수 N이 주어진다. (3<=N<=100)
# 둘째줄에 공백으로 구분되어 각 식량창고에 저장된 식량의개수 K가 주어진다. ( 0<= K <=1,000 )
# 
# 입력조건
# 첫째줄에 N(2<=N<=100,0000), K(2<=K<=100,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다. 이때 N은 K보다 항상 크거나 같다.
# 
# 출력조건 
# 첫쨰 줄에 개미전사가 얻을 수 있는 식랴의 최댓값을 출력하시오.


# 점화식 풀이 진짜 기가막히고 코가 막힙니다잉 그지요~

# 정수 N을 입력받기
n = int(input())
#모든 식량 정보 입력받기
array = list(map(int, input().split()))
#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100
# 다이나믹 프로그래밍 (Dynamic Programming) 진행(바텀업)
d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1] , d[i-2] + array[i])

# 계산된 결과 출력
print(d[n-1])