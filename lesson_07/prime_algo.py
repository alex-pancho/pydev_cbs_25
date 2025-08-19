from collections import Counter

def is_prime(n):
    """Перевіряє, чи є число простим."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Розкладає число на прості множники."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    counted = Counter(factors)
    return [f"{p}**{k}" if k > 1 else p for p, k in counted.items()]

def generate_dict(start, end):
    """Генерує словник: число -> 1 (якщо просте) або список простих множників."""
    result = {}
    for number in range(start, end + 1):
        if is_prime(number):
            result[number] = 1
        else:
            result[number] = prime_factors(number)
    return result

# Приклад використання:
start = 2
end = 201
dictionary = generate_dict(start, end)

# Вивід результату:
for k, v in dictionary.items():
    print(f"{k}: {v}")