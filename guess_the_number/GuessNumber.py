from random import randint as rand

attempts = 0
oneMore = 'д'

print('Привет, попробуй угадать число от 1 до 100. Введи свое имя, чтобы начать.')
gamer = input('Как твое имя? ')
while(oneMore.upper() == 'ДА' or oneMore.upper() == 'Д'):
    hiddenNumber = rand(1, 100)
    print(gamer+' у тебя 6 попыток. Удачи!')
    for attempts in range(6):
        guess = int(input('Какое число загадано? '))
        if guess < hiddenNumber:
            print('Загаданное число больше!')
        if guess > hiddenNumber:
            print('Загаданное число меньше!')
        if guess == hiddenNumber:
            break
    if guess == hiddenNumber:
        print(gamer+' поздравляю, ты капитальный красавчик!!! Угадал с '
              +str(attempts)+' попытки.')
    if guess != hiddenNumber:
        print('Видимо сегодня не твой день '+gamer+'. Было загадано число '
              +str(hiddenNumber))
    oneMore = input('Чтобы сыграть еще раз? да или нет?  :')
