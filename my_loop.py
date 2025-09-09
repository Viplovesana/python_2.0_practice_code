
'''
name = "viplove"
for i in name:
    print(i)
    if(i =="l"):
        print("this l is so spaicial")'''


'''colors = ["red","green","yellow","black","orange"]
for color in colors :
    print (color)
    for i in color:
        print (i)'''


# for k in range(1,20001):
#     print(k)

# for k in range(1,20,5):
#  print(k)

# ..............while loop................

'''i = 0
while(i<5):
    print(i)
    i=i+1
print("loop is completed")   ''' 


'''i = int(input("Enter the number :"))

while(i <= 40):
    i = int(input("Enter the number :"))
    print(i)
print("loop is done")  '''  

'''number =       5
while(number>0):
    print(number)
    number=number-1

else:
    print("i am inside the else") '''

# ............print a table using a loop.......

'''for i in range(11):
    if (i == 10):
        break
    print("5 *",i+1,"=",5*(i+1))
'''

'''for i in range(12):
    if (i == 10):
        print("skip the itration")
        continue
    print("5 *",i,"=",5*i) '''   
    
# ............do while...............................

'''num = 0 
while True:
    print(num)
    num = num +1
    if (num == 101):
        break'''
    
'''
for k in range (10,1001):
    print(k)  '''
'''
for i in range (1,20,5):
    print(i)'''

# xample 1: Write a program to display n natural numbers. (In Horizontal-

'''for i in range (0,11):
    print(i)'''

#Write a program to calculate the sum of numbers. 
'''
sum = 0
for i in range (1,11):
    sum=sum+i
    print ("the sum of",i,"is",sum)'''

# Example 3: Write a program to find even no. (2,4,6,8,….) 
'''
for i in range (1,11):
    print("2*",i,"=",i*2)'''

# Example 4: Write a program find odd no.(1,3,5,7,9,……) 

'''for i in range(1,21):
    print("the all odd no is",i*3)

for i in range(1,21,2):
    print(i)    
'''
# Example 5: Write a program to find factorial of given no. 

'''fact = 1
n = int(input("Enter the number :")) 
for i in range(1,n+1):
    fact=fact*i
print("the factorial :",fact)

fact = 1
for i in range(1,21):
    fact=fact*i
    print("the factorial of",i,"is :",fact)'''


# Example 6: Write a program to print your names ten times.       

'''name="viplove"
for i in range(1,11) :
    print(i,name)'''


# ......................................While loop.....................................................................

# Write a program to display n natural numbers. 
'''
n = int(input("Enter the no :"))
print(f"first {n} natural no are ")
i = 1
while i <= n:
    print (i,end=" ")
    i = i + 1'''

# Write a program to calculate the sum of numbers. 
'''
n = int(input("Enter the no :"))
sum = 0 
i =1 
while i <= n:
    sum = sum+i
    print(sum)
    i=i+1'''


# Print numbers until user enters 0

'''n = int(input("Enter the no :"))

while n != 0:
    print("you enterd ",n)
    n = int(input("Enter the no :"))'''

# Write a program to find even no. (2,4,6,8,….) 

'''n= int(input("Enter the number where you stp :"))

i = 1 
while i <= n:
    print(i*2)
    i=i+1'''

# Write a program find odd no.(1,3,5,7,9,……) 

'''num=int(input("Enter the number :"))
i=1
while i<=num:
    print(i*3)
    i=i+1'''

# Write a program to find factorial of given no. 
'''num = int(input("enter the number :"))
fact = 1
i = 1
while i<=num:
    fact=fact*i
    print(fact)
    i=i+1'''
# Write a program to print your names ten times. 
      
'''name =str(input("Enter your name :"))
n = int(input("Enter the number :"))

i = 1
while i<=n:
    print(name)
    i = i + 1'''

# Write a program to find how many vowels and consonants are present in strings. 

'''string=str(input("Enter the string :"))

vowels="aeiouAEIOU"
vowel_count = 0
consonant_count = 0
i = 0
while i < len(string):
    char=string[i]
    if char.isalpha():
        if char in vowels:
            vowel_count=vowel_count+1
        else:
            consonant_count=consonant_count+1
        i = i + 1    
print( "vowel is ",vowel_count)
print("consonant is ",consonant_count)  '''   

# Example 8: Write a program to add 5 in each elements in given list.  
# [10,20,30,40,50] 

'''l = [10,20,30,40,50] 
i = 0
while i < len(l):
    l[i]=l[i]+5
    i=i+1
print(l)  ''' 

# Example 9: Write a program to add 5 in each elements in given tuple. (10,20,30,40,50) 

'''tple = (10,20,30,40,50)

l = list(tple)
i = 0
while i < len(l):
    l[i]=l[i]+5
    i=i+1
    tple=tuple(l)
print(tple) '''

# Example 10: Write a program to create a list from given string.  

'''string = "viplove","riohan","piyush"
list = list(string)
print(list)'''



# .............................................forloop......................................................................>>

# Example 1: Print the first 10 natural numbers using for loop. 

'''for i in range(1,11):
    print(i)'''

# Python program to print all the even numbers within the given range. 

'''for i in range(1,21):
    print(i*2)'''
'''
n = int(input("Enter the no :"))
i = 1
while i <= n:
    print(i * 3)
    i=i+1'''

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number. 

# for
'''sum  = 0
for i in range(1,11):
    sum=sum+i
    print(sum)
'''

# while
'''n =int(input("Entyer the No :"))
sum=0
i = 1
while i<=n:
    sum=sum+i
    print ("rhe sum of ",i ,"is",sum)
    i=i+1
'''

# Python program to calculate the sum of all the odd numbers within the given range. 
# forloop
'''sum = 0
for i in range(1,20):
    if i % 2 !=0:
        sum=sum+i  
        print(i,sum)'''

# while
'''n = int(input("Enter the no :"))
sum=0
i=1
while i<= n:
    if i % 2 != 0:
        sum = sum + i
        print("sum of odd no",sum)
    i=i+1    '''


# Example 5: Python program to print a multiplication table of a given number 
# for
'''n = int(input("Enter the no :"))
for i in range(1,11):
        print(n,"x",i,"=",n*i)
'''

# while
'''num = int(input("Enter the number :"))
i = 1
count = 10
while i <= count:
    print(num,"x",i,"=",num*i) 
    i=i+1   '''       

# Example 6: Python program to display numbers from a list using a for loop. 

# for
'''lst = [1,2,3,"viplove",5,6,"neerajsir",8,9,10]
print(lst)

for i in lst:
    if type(i) == int:
        print(i)'''

# while
'''lst = [1,2,3,"viplove",5,6,"neerajsir",8,9,10]
i = 0
while i < len(lst) :
    if type(lst[i]) == int:
        print(lst[i])
    i = i+1'''

# Example 7: Python program to count the total number of digits in a number. 
# for 
'''num = [1,2,3,4,5,6,8,9,10,23,54,2,65,32,"bsdj",2]
tdgt = int(len(num))
print ("total no of digits in num are",tdgt)

for i in num:
    if type(i) == int:
        print(i)'''
'''   
num = [1,2,3,4,5,6,8,9,10,23,54,2,65,32,"bsdj",2]

i=1
while i <= len(num):
    if type(i) == int:
        print(i)
    i=i+1'''

# Example 8: WAp whether  the word is palindrome or not 

'''word = "madam"
rev = ""                                                             
for char in word:
    rev = char + rev
if word == rev:
    print(word,"is palindrom")
else:
    print (word," is not palindrom")    '''

# while 
'''word ="madam"
rev =""
i = 0
while i < len(word):
    rev = word[i] + rev
    i = i + 1
if word == rev:
    print(word,"is palindrom")
else:
    print(word,"is not a palindrom")    ''' 

# Python program that accepts a word from the user and reverses it. 

'''string = input("enter any name :") 
rev = ""
for char in string:
    rev = char +rev
if rev == string:
    print (string,"is plaindrom")
else :
    print(string,"is not a palindrom") '''   


# Example 11: Python program to count the number of even and odd numbers from a series of numbers. 

'''l = [5,8,5,2,9,2,6,7,8,5,]
even_count=0
odd_count=0
for i in range(len(l)):
    if l[i] % 2 == 0:
        even_count=even_count+1
        print(l[i],"is even")
    else:
        odd_count = odd_count +1
        print(l[i],"is odd") 
print("total count of even",even_count)
print("total count of odd",odd_count)    '''  

# while 

l = [5,8,5,2,9,2,6,7,8,5,]
even_count=0
odd_count=0
i = 0 
while i < len(l):
    if l[i] % 2 == 0:
        even_count=even_count+1
        print(l[i],"is even")
        i=i+1
    else:    
        odd_count = odd_count +1
        print(l[i],"is odd") 
        i=i+1
print("total count of even",even_count)
print("total count of odd",odd_count)




        
    






    