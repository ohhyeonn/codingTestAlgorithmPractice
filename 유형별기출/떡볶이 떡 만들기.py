# 문제
#
# 많은 데이터와 많은 경우를 다루게 됨으로 이진 탐색을 자연스럽게 생각해내야된다.
# 그리고
# 이진탐색의 핵심은 반반 짜르면서 근접하는거기때문에 더이상 짜를 것이 없을때가 제일 근접한것임을 알면되겟다 (ex start와 end가 역전되는 경우)




# 입력조건
# 첫째줄에 떡의 개수 N과 요청한 떡의 길이M이 주어진다. (1 <= N <= 1,000,000 ,     1<= M <=2,000,000,000)
# 둘째줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은필요한 양만큼 떡을 사간 수 있따. 높이는 10억 보다 작거나 같은 양의정수 또는 0이다.


# 출력조건
# 적어도 M만큼의 떡을 가져가기위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

# 입력 예시
# 4 6 
# 19 15 10 17
# 출력 예시
# 15



# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n , m = list(map(int , input().split(' ' )))
# 각떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 떄의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자른기(왼쪾부분 탐색)
    if total < m:
        end = mid -1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 떄가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)