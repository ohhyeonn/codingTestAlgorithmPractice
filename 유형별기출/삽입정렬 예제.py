# 배열이 있다.
# 첫번째 인덱스녀석을 뒤로보내며 위치시킴으로서 삽입할곳을 찾는다.
# 두번째 인덱스녀석을 뒤로보내며 위치시킴으로서 삽입할곳을 찾는다.
# .. 요런식

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range( i, 0 , -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else : # 자기보다 작은 데잍어를 만나면 그 위치에서 멈춤
                break

print(array)