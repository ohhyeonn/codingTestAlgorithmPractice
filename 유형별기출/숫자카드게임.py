# 문제
# 숫자카드게임은 N*M의 2차원 배열에서 각행에서 가장 작은 수들중에서 제일 큰 값을 뽑는 문제이다.
# 입력예시 
# 3 3 
# 3 2 1
# 4 1 4
# 2 2 2 
# 결과값 : 2
#
# 입력조건
# * 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M 이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= N , M <= 100)
# * 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000이하의 자연수이다.
#
# 출력조건
# * 첫째줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.



# min() 함수를 이용한 풀이

# N , M 을 공백으로 구분하여 받는다.
n , m = map(int, input().split())

result = 0

# 한줄씩 입력받으면서 바로 확인하는 식으로 구현한다.
for i in range(n):
    data = list =(map(int, input().split()))
    # 현재 줄에서 가장 작은수를 찾는다.
    min_value = min(data)
    # 가장 작은수들 중에서 가장 큰수를 찾는다
    result = max(result, min_value)
# 최종답안 출력
print(result)
