# 입력조건
#
#  
# 첫째줄에 N(<= N <= 1,000) , M (1<= M <= 10,000) , K(1 <= K <= 10,000)의 자연수가 주어지며 , 각자연수는 공백으로 구분된다.
# 
# 둘쨰줄에 N개의 자연수가 주어진다, 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.



# 출력조건
# 
#
# 첫째줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
# 
# 큰수의 법칙 
# 동빈이의 큰수의 법칙은 다양한 수로 이루어진 배열이 있을때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질수 없는것이 이 법칙의 특징이다.
# 예를 들어 순서대로 2, 4, 5 , 4 , 6으로 이루어진 배열이 있을때 M이 8이고 , K가 3 이라고 가정하자.
# 이경우 특정한 인덱스의 수가 연속해서 세 번 까지만 더해질수 있으므로 큰수의 법칙에따른 결과는 6+6+6+5+6+6+6+5 인 46이 된다.
# 단, 서로다른 인덱스에 해당하는 수가 같은경우에도 서로 다른것으로 간주한다. 예를 들어 순서 대로 3, 4, 3, 4, 3 으로 이루어진 배열이 있을때 M이 7이고, K가 2 라고 가정하자. 이 경우 두번째 원소에 해당하는 
# 4와 네번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4*7 = 28 이 된다.


# 입력예시
# 5 8 3
# 2 4 5 4 6
#
# 출력예시
# 46



# 서현오 답안
n , m , k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0
kFlag = 0

for i in range(m):
    if kFlag >= k:
        result += second
        kFlag = 0
    else :
        result += first
        kFlag += 1
    
print(result)


#답지
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




# 비교 정리
# 답지와의 차이점 : 답지는 연속해서 더하고 한번더하고를 while 문으로 구현 나는 그냥 m번 for 문구현 편한형식 취하면 될듯하다
# 개선할 사항
# 없는듯 수열로 하면 좋은데 그건 일단 논외로 두자
