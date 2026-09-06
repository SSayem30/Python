class Car:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        print(f"{name} is running at {speed} Km/h")

car1=Car("BMW",200)
car2=Car("Bugati",300)
print(f"First car's name is {car1.name}")
print(f"Second car's speed is {car2.speed}")