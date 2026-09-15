class Human:
    num_eyes=2
    def __init__(self,arms):
        self.num_legs=2
        self.num_arms=arms
    def display(self):
        self.bro=2
        print("Nice to meet you!!")
class Male(Human):
    def __init__(self,name,arm):
        super().__init__(arm)
        self.name=name
    def display(self,work):
        self.work=work
        super().display()
        print(f"I am {self.name} and i have {self.num_legs} legs, {self.num_arms} arms, {Human.num_eyes} eyes")
        print(f"I am a {work} and i have {self.bro} brothers")
male1=Male("Thomas Shelby",2)
male1.display("Gangster")
h1=Human(2)
h1.display()