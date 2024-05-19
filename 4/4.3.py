v = int(input('введите число '))
s = int(input('введите степень '))
a = 0

def degree(a,number, degr):
    if a==0:
        a=number
    if degr==1:
        print(a)
        return a
    else:
        
        a=a*number
        return  degree(a,number,degr-1)

degree(a,v,s)