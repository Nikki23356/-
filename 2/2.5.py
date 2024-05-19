class library:
    def __init__(self):
        self.name = ['b1', 'b2', 'b3']
    def deleted(self, d):
        a = self.name
        a.remove(d)
        self.name = a
        print(self.name)
    def app (self,add):
        a = self.name
        a.append(add)
        print(self.name)
    def find(self,finding):
        a = self.name
        b = a.count(finding)
        print(b)
        
tom = library()
tom.deleted('b1')
tom.app('b4')
tom.find('b4')