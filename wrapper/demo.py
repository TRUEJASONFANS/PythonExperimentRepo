from functools import wraps
def memory_cashe(fn):
    cache = {}
    miss = object()
    # only instance one time
    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper

@memory_cashe
def fib(n):
    if n < 2:
       return n
    else:
        return fib(n-1) + fib(n-2)
print fib(5)