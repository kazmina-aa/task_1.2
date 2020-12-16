import random
attempt = 1
number = random.randint(0, 9999)
random_n = -1
print('Угадайте число. Оно находится в диапазоне от 0 до 9999:')
while random_n!=number:
    random_n = int(input('Это ваша {0} попытка. Введите число: '.format(attempt)))
    attempt += 1
    if random_n < number:
        print('Ваше число меньше загаданного. Попробуйте еще.')
    if random_n > number:
        print('Ваше число больше загаданного. Попробуйте еще.')
    if random_n == number:
        break
if random_n == number:
    print('Вы угадали число, использовав {0} попыток!'.format(attempt-1))
