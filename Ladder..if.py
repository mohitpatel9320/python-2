sname=input("Enter Student Name : ")
rno=int(input("Enter Student Roll NO : "))
m1=int(input("Enter Marks Of Subject 1 : "))
m2=int(input("Enter Marks Of Subject 2 : "))
m3=int(input("Enter Marks Of Subject 3 : "))

total=m1+m2+m3
per=total/3

print("Student Name : ",sname)
print("Roll NO : ",rno)
print("Total : ",total)
print("Percentage : ",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
