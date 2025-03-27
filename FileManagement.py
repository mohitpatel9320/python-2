file=open("tops2.txt","w")
file.write("This is file management by using python.")
file.close()

print("******************************************************************************")

file=open("tops2.txt","r")
print(file.read())
file.close()
print("file open using read mode.")

print("******************************************************************************")

file=open("tops2.txt","a")
file.write("This is appended Text.")
file.close()
print("File appended successfully.")

print("******************************************************************************")
file=open("tops3.txt","w+")
file.write("This is Write + method Text.")
file.seek(0)
print(file.read())
file.close()
print("file opened using w+ method.")

print("******************************************************************************")

file=open("tops1.txt","r+")
file.write("This is R+ mode using python. ")
file.seek(0)
print(file.read())


