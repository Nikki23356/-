from math import sqrt
a= int(input('введите x1 '))
h= int(input('введите y1 '))
b= int(input('введите x2 '))
r= int(input('введите y2 '))
g= a+b
j= h+r
class grafiky:
        
    def s(self, x, y, x1, y1):
        if x == x1:
            s= abs(y-y1)
        elif y == y1:
            s= abs(x-x1)
        else:
            s= sqrt(g ** 2 + j ** 2) 
        print ('растояние между точками = ', s)
        
    def проверка(self, x,y):
        if x == 0:
            print('первая лежит на OX')
        elif y==0:
            print('первая лежит на OY ')
        else:
            print('первая не лежит ')
            
    def проверка2(self, x,y):
        if x == 0:
            print('вторая лежит на OX')
        elif y==0:
            print('вторая лежит на OY ')
        else:
            print('вторая не лежит ') 
            
w = grafiky()
w.s(a,h,b,r)
w.проверка(a, h)  
w.проверка2(b, r)