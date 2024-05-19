import math
import random 
a = 'armze'
b = 0
n=a
letters=[]
ans=[]
while True:
    for i in range (len(a)):
        letter=random.choice(a)
        letters.append(letter)
        t=list(a)
        t.remove(letter)
        t="".join(t)
    b+=1
    t=n
    if  "".join(letters) not in ans:
        ans.append("".join(letters))
    letters=[]
    if len(ans) == math.factorial(len(t)) :
        break
print(ans)