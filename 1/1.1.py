a='конь собака кошка конь '
b=[]
c=[]
a=a.split()
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
    b.append(a[i])
for i in range(len(c)):
    a.remove(c[i])
a=sorted(a)
print(a)