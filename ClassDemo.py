class Student:
    def getData(self,fname,lname):
        self.f=fname
        self.l=lname
    def putData(self):
        print("First Name: ",self.f)
        print("last Name: ",self.l)
        
s1=Student()
s1.getData("Mohit","Patel")
s1.putData()
