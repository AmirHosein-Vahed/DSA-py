def fibo(n: int):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)


def fibo_dynamic(n: int, memo={}):
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibo_dynamic(n-1, memo) + fibo_dynamic(n-2, memo)
    return memo[n]


print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(50))

print(fibo_dynamic(5))
print(fibo_dynamic(6))
print(fibo_dynamic(7))
print(fibo_dynamic(60))