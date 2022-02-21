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




# 아래 나올거는 위에보다 좀 더 비효율적인데 
# 위에는 피벗과의 비교를 최소화 하는 로직이 포함되어있는데
# 아래는 피벗과의 비교를 최소화없이 다 하게 되어있어서 비효율 적이라고 할 수있다.
# 대신 이해하기 쉽게 직관적이다.

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫번째 원소로 한다.
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [ x for x in tail if x <= pivot] # 분활된 왼쪽부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))