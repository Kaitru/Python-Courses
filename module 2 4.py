numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    flag = True
    for j in range(2, numbers[i] - 1):
        if numbers[i] % j == 0:
            flag = False
            continue
    if flag and numbers[i] != 1:
        primes.append(numbers[i])
    elif numbers[i] != 1:
        not_primes.append(numbers[i])

print(primes)
print(not_primes)
