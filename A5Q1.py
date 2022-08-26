# Write a Python class to implement pow(x, n)

class Calculation :

    def __init__(self,number,Index):
        self.number = number
        self.Index = Index
    def Pow(self):
        if self.Index > 0 :
            i = 0
            m = 1
            while i < self.Index :                 
                m  = self.number * m               
                i  += 1
        elif self.Index < 0 :                   
            i = 0
            m = 1
            while i > self.Index :     
                m  = self.number * m  
                i = i - 1
                m = 1/m
        else :
            m = 1

        return m  


a = int(input("Enter the Number : "))    
b = int(input("Enter the power of the Number : "))


p = Calculation(a,b)
print(f"{a} raised to the power {b} is {p.Pow()}")