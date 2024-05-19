a= input('введите наиминование товара ')
b= int(input('введите количества товара '))
c= int(input('введите цену товара '))
j=0
class shop:
    def __init__(self):
        self.name = 'a'
        self.number = b
        self.cost = c
    def changeNumber(self, change):
        j = int(input('скольно прибавиь/убрать? '))
        j=j
        N = input('прибавить или вычесть(+/-) ')
        if N == '+':
            self.number += j
            print('конечное число товаров', self.number)
        if N == '-' and j <= self.number:
            self.number -= j
            print('конечное число товаров', self.number)
        elif j >= self.number:
            print('нет столько товаров')
    def общ_цен(self):
        all = self.number * self.cost
        print('итоговая цена', all)

tom = shop()
tom.changeNumber(j)
tom.общ_цен()