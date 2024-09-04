#재귀함수를 이용한 fibo
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
# print(fibonacci(3))

#동적계획법 활용
def fibo_dp(num):
    cache = [ 0 for index in range(num+1) ]
    cache[0] = 0
    cache[1] = 1
    
    for i in range(2,num+1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[num]


