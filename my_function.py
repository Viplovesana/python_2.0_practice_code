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
num = int(input("Enter the number :"))
print("The sum upto the given no ")
def sum_no(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
        
        print(sum)
    print(sum,"is the only sum of given number")    
sum_no(num)

         
