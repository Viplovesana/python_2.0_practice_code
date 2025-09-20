'''
def func_name(a,b):
  sum = a+b
  print(sum)  
  return a + b

result = func_name(37,9)
print("the result is",result)

print("after return")
func_name(34,94)
'''


# Wap to print the lenght of a list ................

'''heros = [ "ironman","shaktiman","spiderman"]

cities = ["dewas","bhopal"]

def list_para(list):
  print(len(list))
  return list
list_para(heros)
list_para(cities)'''

# Wap to print the list in single line  ................

'''fruits = ["grapes","orange","apple","mango"]

def list_fruits(list):
    for i in list:
      print(i,end=", ")
list_fruits(fruits)   ''' 

# Waf to find a factorial using functions.............

'''num = int ( input("Enter the number :"))

def find_fac(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i   
    return factorial
result=find_fac(num)
print(result,"this is the fact of",num)  '''

# WAF to convert usd into indian rupees or inr 
'''currency = int(input("Enter the USD "))
def converter(usd):
    inr = usd * 83
    print(currency,"USD is equals too",inr,"in inr")
converter(currency)    '''

# Example 1: Print the first 10 natural numbers using for funtion.

'''for i in range(0,11):
    print(i)''' 
'''def natural_no(a,b): 
    for i in range(a,b+1):
        print(i)
natural_no(0,10)'''   

# Example 2: Python program to print all the even numbers within the given range using functions.
'''def even_no(a,b):
  for i in range(a,b):
   print(i*2) 
even_no(0,11) '''   

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number using function.
'''num = int(input("Enter the number :"))
print("The sum upto the given no ")
def sum_no(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
        
        print(sum)
    print(sum,"is the only sum of given number")    
sum_no(num)
'''
# Example 4: Python program to calculate the sum of all the odd numbers within the given range using fuction.

'''def odd_sum(a,b):
    sum = 0
    for i in range(a,b+1):
        if i % 2 !=0: 
          sum = sum + i
          print(sum)
odd_sum(1,20)          
         '''
# Example 5: Python program to print a multiplication table of a given number using function..
'''num = int(input("Enter the number :"))
def table(n):
    for i in range(1,11):
        tab = n*i
        print(num,"x",i,"=",tab)
table(num)  '''      

# Example 6: Python program to display numbers from a list using a for loop unsing function.
# for numbers
'''num = [ 1,2,3,4,5,6,"viplove","ananya",7,8]
def num_list(list):
    for i in list:
        if type(i) == int:
            print(i)   
num_list(num)
# for strings
num = [ 1,2,3,4,5,6,"viplove","ananya",7,8]
def num_list(list):
    for i in list:
        if type(i) == str:
            print(i)   
num_list(num)
'''

# Example 7: Python program to count the total number of digits in a number using function. 
         
'''num = [1,20,3,4,54,66,7,"viplove sana","anu",8,9]

def digit_count(list):
    count =0
    for i in list:
        if type(i) == int:
            count = count + 1
            print(i)
    print("total count is",count,"is in the given list")
digit_count(num)   '''    

# Example 8:  .(madam=madam) WAF cheack weathe3r the string is palindrome or not 
'''name = input("Enter the name :")

def palindrome(string):
    rev = ""
    for char in string:
        rev = char + rev
    if rev == string:
     print("the given string is plindrom")
    else:
      print("not an palindrom")    
palindrome(name)  '''    


# Python program that accepts a word from the user and reverses using function.


'''name = input("Enter the name  :")

def reverse(string):
    rev = ""
    for i in string:
        rev = i + rev
    print(rev,"is the reverse of given string")  
reverse(name)    '''   
    
# Example 10: Python program to check if a given number is an Armstrong number. (153=1**3+5**3+3**3) using function.......
'''

def arm_strong(num):
    number = num
    total = 0 
    power = len(str(number))
    while number > 0:
        last_digit = number % 10
        total = total +(last_digit ** power)
        number = number // 10
    if total == num:
        print("the no is armstronge")
    else:
        print("not an armstronge")
n = int(input("Enter the number :"))                    
arm_strong(n)  ''' 
# the whole process of arm stronge .....................
'''
Iteration 1:
last_digit = 153 % 10 = 3
total = 0 + 3**3 = 27
temp = 153 // 10 = 15

Iteration 2:
last_digit = 15 % 10 = 5
total = 27 + 5**3 = 27 + 125 = 152
temp = 15 // 10 = 1

Iteration 3:
last_digit = 1 % 10 = 1
total = 152 + 1**3 = 153
temp = 1 // 10 = 0'''


# Example 11: Python program to count the number of even and odd numbers from a series of numbers using functions.

'''n = [1,2,3,4,5,6,7,8,9,22,34,65,76,87,23,83,686]
def odd_even(num):
    odd_count = 0
    even_count = 0
    for i in num:
        if i % 2 == 0 :
            even_count = even_count + 1        
        else:
            odd_count = odd_count + 1                  
    print(even_count,"is the total count of even no")
    print(odd_count,"is the total count of odd no") 
   
odd_even(n)'''

# Example 12: Python program to display all numbers within a range except the prime numbers using functions...

number = int(input("Enter the number :"))

def all_num(n): 
    for num in range(1,n+1):
        if num == 1:
            print(num)
            continue
        for i in range(2,num):
              if num % i == 0:
                  print(num)       
                  break       
all_num(number)  
    
    
    

  