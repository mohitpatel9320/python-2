import random


#print(random.randint(1,50))
#print(random.choice([10,1,"tops","java",True,100,200]))

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
