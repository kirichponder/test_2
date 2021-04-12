print("Деление - 1 \nУмножение - 2")

o = int(input("Enter: "))

a = int(input('а: '))
b = int(input('b: '))

def umn(o,a,b):
    if o == 2:
        return a*b
    elif o == 1:
        return a/b
        
    
print(umn(o,a,b))