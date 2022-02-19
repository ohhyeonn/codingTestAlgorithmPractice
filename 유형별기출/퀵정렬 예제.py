# 퀵정렬은 살짜쿵 특이하다.
# 삽입정렬은 정렬이 어느정도 되어 있으면 빠르고
# 퀵정렬은 정렬이 어느정도 되어있지 않아야 빠르다.

# 피벗이란게 있는데 각 함수호출의 맨처음 index의 원자를 피벗으로 정한다. 이피벗을 기준으로 작은놈은 왼쪽 큰놈은 오른쪽 피벗은 그가운데 이런식으로 2분할 해가며
# 각 분할들에게 재귀스로 정렬을 완료시킨다.
# 이때 정렬할분할이 1개면 정렬이 이미 끝낫다고 보는것으로 재귀를 탈출스한다 ㅇㅇㅋ


array= [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end 


    while left <= right:
        # left는 피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right는 피벗보다 작은 데이터를 찾을때까지 반복  ( 책에서는 while right > start and ~~ 인데 아래처럼이 더 통일성스 있네 ㅇㅇ 저거 조건틀리면 무한 뤂 간다 ㅇㅇ! )    
        while right >= start+1 and array[right] >= array[pivot]:
            right -= 1
        if left > right : # 엇갈렸다면 작은데이터와 피벗을 교체
            array[right] , array[pivot] = array[pivot], array[right]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right] , array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right +1 , end)

quick_sort(array, 0, len(array)-1)
print(array)
