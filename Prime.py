def isprime(number):
    count=0
    if number<2:
        count=2
    for i in range(2,number):
        if number%i==0:
            count=1
    if count==0:
        print("Prime number!!!")
    else:
        print("Not Prime number.")    

n=int(input("Enter the number: "))
isprime(n)