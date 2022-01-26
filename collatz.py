def X_input ():
  while True:
    n = int(input('Введите натуральное число:'))
    if n > 0:
      break
    print('Неверные данные')
  return n


def x2 (n):
  return collatz(n//2)


def x3_1 (n)
  return collatz(n*3+1)


def collatz (x)
