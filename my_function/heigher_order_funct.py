

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

from functools import reduce 

num = [1,2,3,4,54,6]
def mysum (x,y):
    return x+y 
sum = reduce(mysum,num)
print(sum)