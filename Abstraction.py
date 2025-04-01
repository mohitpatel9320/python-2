from abc import ABC,abstractmethod

class RBI(ABC):
    def show(self):
        print("Show From RBI.")

    @abstractmethod
    def roi(self,r):
        pass
    
class SBI(RBI):
    def show(self):
        super().show()
        print("Show From SBI.")

    def roi(self,r):
        print("Rate of intrest Given By SBI Is : ",r)

class HDFC(RBI):
    def show(self):
        print("Show From HDFC.")

    def roi(self,r):
        print("Rate of intrest Given By HDFC Is : ",r)

s1=SBI()
s1.show()
s1.roi(6.5)

h1=HDFC()
h1.show()
h1.roi(7.5)
