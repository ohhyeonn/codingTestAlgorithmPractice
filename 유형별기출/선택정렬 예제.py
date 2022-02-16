# 배열이 있다.
# 첫번째 인덱스에 들어갈 놈을 선택해서 첫번째 인덱스 자리에 넣는다.
# 두번째 인덱스에 들어갈 놈을 선택해서 두번쨰 인덱스 자리에 넣는다.
# .. 요런식

array = [ 7 , 5, 9 , 0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index]  = array [min_index], array[i] # 스와프

print(array)