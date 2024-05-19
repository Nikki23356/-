class trianglleChecker:
    def check(self, a,b,c):
        if a+b>c and a+c>b and b+c>a:
            print('можно строить треугольник')
        else:
            print('нельзя строить')
    def minus(self, a,b,c):
        if a<0 or b<0 or c<0:
            print('нельзя с отрицательными числами')
    def letters(self, a,b,c):
        if a == str or b == str or c == str:
            print('вводи только числа, алёша')
     
            
tom = trianglleChecker()
tom.check(13, 30, 21)
tom.minus(13, 30, 21)
tom.letters(13, 30, 21)