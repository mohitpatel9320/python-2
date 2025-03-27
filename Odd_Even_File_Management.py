import random

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")
l=data.read().split(",")[:-1]



for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

    if i==1:
        print("it is not a prime number")
    if int(i)>1:
        for j in range(2,int(i)):
            if int(i)%j==0:
                # print(i," is not a prime number.")
                break
        else:
            # prime.write(int(i),",")
            prime.write(f"{i} ,")

data.close()
even.close()
odd.close()
prime.close()

data=open("data.txt","r")
even=open("even.txt","r")
odd=open("odd.txt","r")
prime=open("prime.txt","r")

print(data.read())
print(even.read())
print(odd.read())
print(prime.read())

data.close()
even.close()
odd.close()
prime.close()
