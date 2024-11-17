
def is_prime(func):
    def check(*args, **kwargs):
        result = func(*args, **kwargs)
        x = 0
        y = result
        while y:
            if result % y == 0:
                x += 1
            y -= 1

        if x <= 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return check


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 2)
print(result)