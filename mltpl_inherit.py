class Animal:
    def __init__(self,name):
        self.name=name
        self.eyes=2
        print("Animal init is called")
    def sound(self):
        print("Makes sound")
class Bird:
    def __init__(self,skill):
            self.specialty=skill
            self.num_wings=2
            print("Bird init is called")
    def sound(self):
        print("Bird is Chirping")
class Eagle(Animal,Bird):
    def __init__(self,name,eyes,speciality):
         Animal.__init__(self,name)
         Bird.__init__(self,speciality)
         print("Eagle init has been called")
    def sound(self):
        print("Eagle is Screeching")
        Bird.sound(self)
        Animal.sound(self)
    def display(self):
        print(f"{self.name} has {self.eyes} eyes and it can {self.specialty}")
eagle1=Eagle("Eagly",2,"Hunt")
print(f"Eagle has {eagle1.eyes} eyes")
eagle1.display()
# eagle1.sound()
# Bird.sound(eagle1)