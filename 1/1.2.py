a = [13,56]
b = []
c = a[0]
while c!=a[1]:
    hardWord = False
    for j in range(2,c//2):
        # print(j)
        if c%j==0 and c!=j:
            hardWord=True
            break
    if hardWord == False:
        b.append(c)
    c+=1
s=sum(b)
print(s)