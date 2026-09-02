def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print('Math Error')
    else:
        return a/b

operations={
            "+":add(),
            "-":sub(),
            "*":mul(),
            "/":div()
        }
count=True
while count:
    op=input("What operations you want to do(+,-,*,/) and if no enter 'z': ")
    if op=='z':
            count=False
            print("Have a niche day")
    else:
        num1=float(input("Enter the 1st number: "))
        num2=float(input("Enter the 2nd number: "))
        for i in operations:
            if op==i:
                print(f"{num1} {op} {num2} = {operations[i]}")