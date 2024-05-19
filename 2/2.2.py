class Soda:
    def show_me_soda(self,d):
        if d == '':
            print('обычная')
        else:
            print('Газировка с', d)
            
tom = Soda()
tom.show_me_soda('')