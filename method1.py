class CarDesign:
    count=0
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def display(self,specialty):
        self.specialty=specialty
        print(f"{self.name} is running at {self.speed} Km/h and its specialty is {specialty}")
        CarDesign.count+=1
        
car1=CarDesign("BMW",200)
car2=CarDesign("Supra",300)
car1.display("Luxury")
car2.display("Sports")
print(f"There are {CarDesign.count} cars designed")