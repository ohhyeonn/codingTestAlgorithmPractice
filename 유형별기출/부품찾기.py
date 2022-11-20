# 입력조건
# 첫째 줄에 정수 N이 주어진다 ( 1 <= N <= 1,000,000)
# 둘째줄에 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하 이다.
# 셋째줄에는 정수 M이 주어진다. ( 1 <= M <= 100,000)
# 넷째줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000이하 이다.

# 출력조건
# 첫째줄에 공백으로 구분하여 각부품이 존재하면 yes 없으면 no를 출력한다.



# 방법에는 여러가지가 있다. 물론 더있겠지
# 1. 이진탐색 알고리즘이용
# 2. 계수정렬 알고리즘 이용
# 3. 집합자료형 이용(python한정)

# 구현 문제인데 중요한건 1,000,000 인거 그니까 대충찾으면 안되고 효율 좋게 찾는 알고리딈 짜라이거임 ㅇㅇㅋ






# 이진탐색 
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #찾은경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1 
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
        
    return None


# N(가게의 부품 개수 ) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M (손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 전호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i , 0 , n -1)
    if result != None:
        print('yes' , end=' ')
    else :
        print('no', end=' ')








# 계수정렬
# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x :
#     if array[i] == 1:
#         print('yes' , end= ' ')
#     else :
#         print('no', end=' ')





#집합자료형
# n = int(input())
# array = set(map(int, input().split()))

# m = int(input())
# x= list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print('yes', end= ' ')
#     else :
#         print('no', end=' ')

