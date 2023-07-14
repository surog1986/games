from random import randint as rand

attempts = 0
oneMore = 'д'

def attempt(attempts):
    if attempts == 1:
       return(str(attempts)+' попытку.') 
    elif attempts <=4:
        return(str(attempts)+' попытки.')
    else:
        return(str(attempts)+' попыток.')
    
print('Привет, попробуй угадать число от 1 до 100. Введи свое имя, чтобы начать.')
gamer = input()
while(oneMore == 'д' or oneMore == 'Д'):
    hiddenNumber = rand(1, 100)
    print(gamer+' у тебя 6 попыток. Удачи!')
    for attempts in range(6):
        guess = int(input())
        if guess < hiddenNumber:
            print('Загаданное число больше!')
        if guess > hiddenNumber:
            print('Загаданное число меньше!')
        if guess == hiddenNumber:
            break
    if guess == hiddenNumber:
        print(gamer+' поздравляю, ты капитальный красавчик!!! Угадал за '
              +str(attempt(attempts+1)))
    if guess != hiddenNumber:
        print('Видимо сегодня не твой день '+gamer+'. Было загадано число '
              +str(hiddenNumber))
    oneMore = input('Чтобы сыграть еще раз введи "д"  :')
