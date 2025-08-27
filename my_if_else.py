

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

x = int(input("Enter the number : "))

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
        print(x)

#............................................................  
         















