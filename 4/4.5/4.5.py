import csv

def middle( data):
    t=0
    number = 0
    for u in data:
        if u[0]!= 'п»ї12':
            b = u[0]
            start = b.find(';')
            end =b.find(';',start+1)
            a=b[start+1:end]
            
            a1 = int(a)
            t+=a1
            number+=1
    sr = t//number
    print('среднее арифметическое:', sr)

file = open("4.5.csv", "r")
data = csv.reader(file)
middle(data)
file.close()