class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def perimeter(self):
        return 2*(self.a+self.b)
        
    def volume(self):
        return (self.a*self.b)
    
shape=Rectangle(3,6)
print("Perimeter: ",shape.perimeter())
print("Volume area: ",shape.volume())
        