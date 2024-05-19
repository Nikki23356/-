file = open("4.2.txt", 'r')
data = file.readlines()

for a in range(len(data)):
    word1 = 0
    if a==0:
        for i in data:
            if data[a]==i:
                word1+=1
        print(data[a], word1)
    if a>0 and data[a]!=data[a-1]:
        for i in data:
            if data[a]==i:
                word1+=1
        print(data[a], word1)
    
file.close()