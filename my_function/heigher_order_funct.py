

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

cube = lambda x : x * x * x
print(cube(5))

average  = lambda x ,y,z :(x+y+z)/3 
print(average(20,30,50))

def apple(fx,value): 
    return 2 + fx(value)

result = (apple(lambda x : x * x * x,2))
print (result)