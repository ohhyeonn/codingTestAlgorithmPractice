# 피보나치 함수 소스 코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo( x - 1) + fibo(x -2 )

print(fibo(4))



# 다이나믹 프로그램으로 짠 피보나치 함수 소스 코드
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')' , end = ' ')
    if x== 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo( x - 1) + pibo(x - 2)
    return d[x]

print(pibo(4))


