import random

a = int(input(' 1-камень, 2-бумага, 3-ножницы '))
n = random.randint(1, 3)
if a == n:
    print('ничья')
else:
    if a==3 and n==1:
        print('камень')
    elif a == 3 and n==2:
        print('ножницы')
    elif a==1 and n==3:
        print('камень')
    elif a==1 and n==2:
        print('бумага')
    elif a==2 and n==3:
        print('ножницы')
    elif a==2 and n==1:
        print('бумага')