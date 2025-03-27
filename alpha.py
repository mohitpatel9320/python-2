s=input("Enter String:")
al=0
num=0
space=0
totalUpper=0
totalLower=0
space=0

for i in s:
    if i.isalpha():
        al=al+1
        
    elif i.isnumeric():
        num=num+1
    
    elif i.isspace():
        space=space+1

    if i.isupper():
        totalUpper=totalUpper+1

    elif i.islower():
        totalLower=totalLower+1


print("Total alphabats =",al)
print("Total Numerics =",num)
print("Total Upper Case Alphabets = ",totalUpper)
print("Total lowwer Case Alphabets =",totalLower)
print("Total Space = ",space)

