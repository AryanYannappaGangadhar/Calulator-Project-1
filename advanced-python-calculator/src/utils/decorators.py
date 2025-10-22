def timeit(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result

    return wrapper


def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return wrapper