a = input('ввеите слово ')
a = a.replace(' ','')
print(a)
n = a[::-1]
if n==a:
    print('палендром')
else:
    print('не палендром')