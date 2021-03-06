from functools import lru_cache

# maxsize参数是告诉lru_cache，最多缓存最近多少个返回值


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(10)])

fib.cache_clear()
