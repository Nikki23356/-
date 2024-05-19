class Book:
    def name(self,name):
        print(name)
    def avt(self,avt):
        print(avt)
        
tom = Book()
tom.name(input('Введите книгу '))
tom.avt(input('Введите автора '))