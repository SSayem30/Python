class Animal:
    def __init__(self,name):
        self.name=name
        self.eyes=2
        print("Animal init is called")
class Bird(Animal):
    def __init__(self,skill):
            self.speciality=skill
            self.num_wings=2
            print("Bird init is called")
            super().__init__(self)
class Eagle(Bird):
    def sound(self):
        print("Eagle is Screeching")
eagle1=Eagle("Hunt")
print(eagle1.eyes)