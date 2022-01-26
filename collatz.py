def x_input ():
    while True:
        n = int(input('Введите натуральное число:'))
        if n > 0:
            break
        print('Неверные данные')
    return n


def x2 (n):
    return collatz(n//2)


def x3_1 (n):
    return collatz(n*3+1)


def collatz (n):
    result = [n]
    if n == 1:
        pass
    elif n % 2 == 0:
        result.extend(x2())
    else:
        result.extend(x3_1())
    return result


if __name__ == "__main__":
    x = x_input ()
    print (collatz(x))
