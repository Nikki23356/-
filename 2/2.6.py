class avia:
        
    def __init__(self):
        self.company = ['company1','company2','company3']
        self.planes = ['plane1','plane2','plane3']
        self.ways = ['way1','way2','way3']
        print('компании ',self.company)
        print('самолёты ',self.planes)
        print('маршруты ',self.ways)
    def a(self, delcom,delplane,delway):
        self.company.remove(delcom)
        self.planes.remove(delplane)
        self.ways.remove(delway)
    def b (self,addcom,addplane,addway):
        self.company.append(addcom)
        self.planes.append(addplane)
        self.ways.append(addway)
        # print(self.company)
        # print(self.planes)
        # print(self.ways)
    def d(self,findcom,findplane,findway):
        self.company.append(findcom)
        self.planes.append(findplane)
        self.ways.append(findway)
        # print(self.company)
        # print(self.planes)
        # print(self.ways)
        

tom=avia()    
tom.a('company1', 'plane1','way1')
tom.b('company3','plane3','way3')
tom.d('company2','plane2','way2')