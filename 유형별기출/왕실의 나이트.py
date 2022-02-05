# 문제
# 8*8 의 2차원 배열이 있다.
# 이중의 한점을 입력을 받고 그한점에서 배열내에 움직일수 있는 '나이트 움직임'의 가능 경우수를 출력하는것이 문제이다.
# 
# 
# 입력조건
# a부터 h까지의 한문자와 1부터 8까지의 한숫자를 띄어쓰기 없이 한번씩받는다. ex) a1
# 
#  
# 출력조건 
# 첫째줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) -int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1) , (-1, -2) , (1, -2) , (2, -1) , (2, 1) , (1,2) , (-1 , 2) , (-2 , 1)]

# 8 가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 ㅇ뉘치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다며 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)