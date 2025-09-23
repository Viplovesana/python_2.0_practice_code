

# Lamdaa function.......................

'''def lam_daa(x):
    print(x*2)
    return x
print = lam_daa(5)'''


# /So this is the lamdaa function use in the single line 
'''double = lambda x: x * 2  
print(double(6))

triples = lambda x : x * 3
print(triples(5))'''

'''average  = lambda x ,y,z :(x+y+z)/3 
print(average(20,30,50))'''
'''
cube = lambda x : x * x * x
print(cube(5))

def apple(fx,value): 
    return 2 + fx(value)

result = (apple(lambda x : x * x * x,2))
print (result)'''

# ............MAP................................................................


'''def cube(x):
    return x*x*x
result = cube(2)
print(result)    
'''

# ...Without map function.......................................
'''l = [1,2,3,4,56,6]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)  '''  

# ......with map function........................................
'''l = [1,2,3,4,56,6]
newl=list(map(cube,l))
print(newl)'''  



# FILTER........................................

'''l = [1,2,3,4,56,6]

def fil_func(x):
    return x > 4
newl=list(filter(fil_func,l))
print(newl)'''


# ...REDUCE........................................

'''from functools import reduce 

num = [1,2,3,4,54,6]'''
'''def mysum (x,y):
    return x+y 
sum = reduce(mysum,num)
print(sum)'''

# while using lambda func..........................

'''sum = reduce(lambda x,y : x+y,num)
print(sum)'''


# Square the numbers: You have this list: numbers = [2, 3, 4, 5]. Use map() to create a new list where each number is squared. (Expected output: [4, 9, 16, 25]).
'''
numbers = [2, 3, 4, 5]

def square (x):
    return x*x
newl = list(map(square,numbers))
print(newl)

# using lamda function.........
newl = list(map(lambda x: x * x ,numbers))
print(newl)'''

# Convert to uppercase: You have this list: words = ['hello', 'world', 'python']. Use map() to create a new list where all strings are in uppercase. (Expected output: ['HELLO', 'WORLD', 'PYTHON']).

'''words = ['hello', 'world', 'python']
def capatalize(x):
    return x.capitalize()
newl = list(map(capatalize,words))
print(newl)
# using lamda function.........
newl = list(map(lambda x:x.capitalize(),words))
print(newl)
'''


# filter() Questions...............

# Filter even numbers: You have this list: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Use filter() to create a new list that contains only the even numbers. (Expected output: [2, 4, 6, 8, 10]).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_no(x):
    return x % 2 == 0
newl = list(filter(even_no,numbers))
print(newl)

# Filter long strings: You have this list: names = ['raj', 'anita', 'mohan', 'suresh']. Use filter() to create a new list that contains only the names with a length greater than 4 characters. (Expected output: ['anita', 'mohan', 'suresh']).
