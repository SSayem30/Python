class Circle:
    pi=3.1416
    def __init__(self,radius):
        self.radius=radius
        self.area=self.pi*radius*radius
    def circumference(self):
        print(f"The circumference of the circle is: {2*Circle.pi*self.radius}")

a=float(input("Enter the radius of the circle: "))
circle1=Circle(a)
print(f"The area of the circle is: {circle1.area}")
circle1.circumference()