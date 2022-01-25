x = int(input('Введите положительное число:'))
A = []

if x > 0:
    def x2(x):
        x = x / 2
        return collatz(x)


    def x3_1(x):
        x = x * 3 + 1
        return collatz(x)


    def collatz(x):
        if x == 1:
            A.append(int(x))
            return  x
        elif x % 2 == 0:
            A.append(int(x))
            return x2(x)
        else:
            A.append(int(x))
            return x3_1(x)


    collatz(x)
    print(A)
else:
    print("Введены некорректные данные")
