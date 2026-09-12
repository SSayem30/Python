class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.area=3.14*radius*radius
        
a=float(input("Enter the radius of the circle: "))
circle1=Circle(a)
print(circle1.area)