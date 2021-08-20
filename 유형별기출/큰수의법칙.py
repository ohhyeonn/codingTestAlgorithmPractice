# 문제
# 
# 입력조건
# 첫째줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 
# 출력조건 
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
#
# 큰수의 법칙 주어진 수들을 더해서 만들수 있는 제일 큰수 단 중복이 허용되지만 K번연속으로 더하는건 허락되지 않는다 그리고 같은 수이지만 다른 index를 가진 수는 서로 연속관계가 성립되지 않는다.

# 두가지 방법이있다 
# 직관적으로 생각가능한 방법
# 수열을 이용한 방법



# 직관적으로 생각 가능한 방법
n,m,k = map(int , input().split())
data = list(map(int , input().split()))

data.sort()
first = data[len(data)-1]
second = data[len(data)-2]

result = 0

while True:
    for i in range(k) :
        if m != 0:
            result += first
            m += -1
        else:
            break
    if m != 0:
        result += second
        m += -1
    else:
        break

print(result)


# 수열을 이용한 방법
n,m,k = map(int , input().split())
data = list(map(int , input().split()))

data.sort()
first = data[len(data)-1]
second = data[len(data)-2]


count = int(m/(k+1))*k  # 여기서 int 를 씌워서 정수가 나오게끔 해준다!
count += m%(k+1)

result = 0
result = count * first 
result += (m-count) * second

print(result)

