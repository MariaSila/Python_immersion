# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def isprime(num):
    prime_num = 2
    count = 1
    yield prime_num
    prime_num += 1
    while count < num:
        for div in range(3, int(prime_num**0.5) + 1, 2):
            if prime_num % div == 0:
                break
        else:
            count += 1
            yield prime_num
        prime_num += 2


def isprime_2(num):
    prime_num = 2
    yield prime_num
    prime_num = 3
    count = 2
    yield prime_num
    while count < num:
        prime_num += 2
        for div in range(3, prime_num//2, 2):
            if prime_num % div == 0:
                break
        else:
            count += 1
            yield prime_num


print(*isprime(5))
for num in isprime_2(20):
    print(num, end=', ')
