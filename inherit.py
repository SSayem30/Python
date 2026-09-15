class Human:
    num_eyes=2
    def __init__(self):
        self.num_legs=2
        self.num_arms=2
    def display(self):
        self.bro=2
        print("Nice to meet you!!")
class Male(Human):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def display(self,work):
        self.work=work
        super().display()
        print(f"I am {self.name} and i have {self.num_legs} legs, {self.num_arms} arms, {Human.num_eyes} eyes")
        print(f"I am a {work} and i have {self.bro} brothers")
male1=Male("Thomas Shelby")
male1.display("Gangster")
h1=Human()
h1.display()