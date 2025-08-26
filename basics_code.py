# print("Python folder")

# def Code(n):
#     print(n)

# Code("pytthoncode")


# python_one="django-one"
# python_two="django-two"


# ............variables......................................................................

a = 1 
b = "viplove sana"
c = True
d = None
print(a)
print(b)
print("tupe of a is ",type(a))
print("tupe of b is ",type(b))
print("tupe of c is ",type(c))
print("tupe of d is ",type(d))


# ............................datatype............................

list1 = [1,3,5.6,['viplove'],["apple ,banana"]]
print(list1)
tuple1 = (1,3,5.6,('viplove'),("apple ,banana"))
print(tuple1)
dict1 = {"name":"viplove","age":23,"city":"dewas"}
print(dict1)

# .............................operators..........................

print(5+6)          
print(15-6)
print(15*6)
print(15/6)
print(15//6)
print(15%6)
print(5**6)

# .................................calculator...........................

operator = input("Enter the operator to calculate ")
number1 = int(input("Enter the 1st value to calculate "))
number2 = int(input("Enter the 2nd value to calculate "))

if operator == "+":
    print("result : ",number1+number2 )
elif operator == "-":
    print("result : ",number1-number2 )
elif operator == "*":
    print("result : ",number1*number2 )
elif operator == "/":
    if number1 or number1 == 0:
        print("cants divisble by zero ")
    else:
        print("result : ",number1/number2 )    
else:
    print("invalid")
# ......................................end.......................................









