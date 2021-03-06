# 문제
# N 이 주어진다. 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시간중에서 3이 하나라도 포함되면 카운트된다.
# 카운트를 N을 받고 카운트를 출력하는 프로그램을 만드세요
# 
# 입력조건
# 첫째 줄에 정수 N이 입력된다. (0 <= N <= 23)
#  
# 출력조건 
# 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시간중에서 3이 하나라도 포함되면 카운트된다.
# 카운트를 N을 받고 카운트를 출력하는 프로그램을 만드세요


# 완전탐색이다.

# 3중 포문으로구현하면 쉽다.
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'포함되어 있다면 카운트 증가
            if '3' in str(i)+ str(j)+str(k):
                count += 1

print(count)

