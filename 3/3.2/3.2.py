import csv
def a():
    with open('3.2ok.csv') as c:
        reader=csv.reader(c)
        for row in reader:
            print (row)
a()