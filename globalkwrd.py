a=10
def display():
    a=40
    def show():
        global a
        a=a+10
        a*=3
        print(a)
    show()
    print(a)
display()
print(a)