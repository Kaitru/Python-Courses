def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
