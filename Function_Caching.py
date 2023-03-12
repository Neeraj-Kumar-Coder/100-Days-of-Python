from functools import lru_cache


def uncached_fibonacci(nth_term):
    if (nth_term < 2):
        return nth_term
    return uncached_fibonacci(nth_term=nth_term - 1) + uncached_fibonacci(nth_term=nth_term - 2)


@lru_cache(maxsize=None)
def cached_fibonacci(nth_term):
    if (nth_term < 2):
        return nth_term
    return cached_fibonacci(nth_term=nth_term - 1) + cached_fibonacci(nth_term=nth_term - 2)


print(uncached_fibonacci(35))
print(cached_fibonacci(35))
