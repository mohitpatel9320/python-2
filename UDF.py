def oddeven(a):
    if a%2==0:
        print(a,"is Even.")
    else:
        print(a,"is odd.")


def maxof2(a,b):
    if(a>b):
        print(a," is max.")
    else:
        print(b," is max.")

def maxof3(a,b,c):
    if(a>b):
        if(a>c):
            print(a," is max.")
        else:
            print(c," is max.")
    elif(b>c):
        print(b," is max.")
    else:
        print(c," is max.")

