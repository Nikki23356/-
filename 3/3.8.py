a = [12,2,2,34,54,65]

def change(a):
    number = len(a) - 1
    for i in range(number):
        for b in range(number-i):
            if a[b] > a[b+1]:
                a[b], a[b+1] = a[b+1], a[b]

change(a)
print(a)