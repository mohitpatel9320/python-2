# function with no argument & no return value.
def printline():
    print("*"*50)
printline()
print("Welcome to user Defined Function In Python.")
printline()

# function with argument but no return value.

def add(a,b):
    print("Addition = ",a+b)

printline()
add(10,20)
printline()

# function with argument and return value.

def sub(a,b):
    return a-b

printline()
sub=sub(10,20)
print("Subtraction = ",sub)
printline()
