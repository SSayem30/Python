def add(*numbers,name):
    print(numbers)
    print(name)
    c=0
    for i in numbers:
        c=c+i
    print(f"Sum is {c}")

add(2,3,6,name='Sayem')