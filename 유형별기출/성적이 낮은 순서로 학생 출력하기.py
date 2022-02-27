
# ㅇㅇ 첫번쨰는 학생숫자를 받고
# 두번째부터 학생이름과 성적을 줄단위로 받는다
# 정렬해서 출력한다.


# 입력조건
# 첫번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
# 두번째 줄부터 N + 1 번쨰 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100 이하의 자연수 이다.

# 출력조건
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.







# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')