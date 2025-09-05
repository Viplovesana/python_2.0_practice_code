

# ..............................if-else-statement------------------------------

'''a = int(input("Enter your Age : "))
print("OK your age is :",a)
print(a>18)
print(a<=18)
print(a == 18)
print(a!=18)
if a>18:
    print("yes you can drive a car")
else:
    print("you cannot drive a car")'''
# ..........................................................

'''
num = int(input("Enter the number :"))
if num < 0:
    print("number is negative")
elif num == 0:
    print("number is zero")
else:
    print("number is positive") 
    print("i am happy now")
print("okkk") '''   

#............................................................

#.............Greeting programm..............................

'''
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timeshr = int(time.strftime('%H'))
print(timeshr)
timesmn = time.strftime('%M')
print(timesmn)
timesec = time.strftime('%S')
print(timesec)

if timeshr < 24:
    print("good evening sir")
elif timeshr == 24:
    print("good m0orning sir")
elif timeshr >= 0 :
    print("good m0orning sir")     
elif timeshr == 12:
    print("good afternoon sir") 
elif timeshr >= 18 or timeshr <=24:
    print("good evening sir")           
else:
    print("have nice day sir")'''

#...........................................................
# .......................MATCH CASE.........................

'''x = int(input("Enter the number : "))

match x:
    case 0 :
        print ("x is zerio")
    case 4 :
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80") 
    case _:
        print(x)'''

#............................................................  
         
'''b = int(input('inter your Age :'))

if b < 18:
    print("your are aligible for driving licence")
elif b > 18:
    print("tour are not eligible for driving")
elif b <=18:
    print("your are know eligible for driving licence")
else:
    print("your not elgible")  '''  

# ....wap to cheack given no is positive......................

'''
n = int(input("Enter the the number :"))

if n > 0:
    print("number is positive ")
elif n < 0:
    print("number is negative")
elif n == 0 :
    print("number is Zero")
else :
    print("no is invalid")  '''  

# ... Write a program to swap two variables without using third variable. ...

'''a = 100    //tuple unpacking way
b = 200
a,b = b,a
print("a is :" ,a  ,"b is :",b)

a = 50
b = 60
a=a+b   //110     // add and sub way
b=a-b   //50
a=a-b   //60
print(a) 
print(b) '''

#....Write a program to swap two variables using third variable. 
'''
a = 100
b = 200
swap = a
a = b
b =swap
print ("the vale of a :",a)
print ("the vale of b :",b)'''

# .Write a program to swap two variables using using Addition and Subtraction.

'''a =100
b =200

a = a+b 
b = a-b 
a = a-b 
print ("the vale of a :",a)
print ("the vale of b :",b)
'''
#Write a program to find squre root of given no/we can use two method to find square root of num is 0.5 and (1/2)

'''n = int(input("Enter the number :"))

squreroot = n ** (1/2)   

print ("thr square root of n numnber is :", squreroot)'''

# Write a program to find largest no among the three inputs numbers. 

'''a = int(input("Enter the first no :"))
b = int(input("Enter the second no :"))
c = int(input("Enter the third no :"))

if a >= b and a >= c:
    print("This is the largest no :",a)
elif b >= a and b >= c:
    print("This is the largest no :",b)
else :
    print ("the largest no is :",c)'''


#  Write a program to find area of  triangle. 

# formula (i/2) base *height
'''
height = int(input("Enter the height of triangle :"))
base = int(input("Enter the base of triangle :"))

area = 0.5*height*base

print("the Area of traiangke is : ",area)'''

# Write a program to find area of square. 

# formula side * side 
'''
side  = int(input("Enter the side of square :"))

area = side * side 

print ("Area of Square is :",area)'''

# Write a program to find given year is leep year or not. 


year = int(input("Enter the year :"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print ("this is a leapp year")
else:
    print ("this is not a leap year")
    


















