# ............................PATTERNS..............................................>
'''
n = int(input("Enter the no :"))

for i in range(1,n+1):
    print("*"*n)  '''
                   
'''n = int(input("Enter the no :"))
for i in range(1,n + 1):
    print("*"*n)'''

'''n = int(input("Enter the no :"))
for i in range(1,n + 1):
    print(" "*(n-i)+"*"*i)'''

'''n = int(input("Enter the no :"))
for i in range(1,n + 1):
    print("*"*i)'''

'''n = int(input("Enter the no :"))
for i in range(1,n + 1):
    print(" "*(n-i)+"A"*(2*i-1))'''


# wap to make a triangle and invert triangle 
'''n = int(input("Enter the no :"))

for i in range(0,n + 1):
    print(" "*(n-i),"A"*(2*i-1))

for i in range(n,0,-1):
    print(" "*(n-i),"A"*(2*i-1))'''


# wap to make a  right triangle and invert and invert of it 
n = int(input("Enter the no :"))

for i in range(0,n + 1):
    print(""*(n-i),"A"*i)

for i in range(n,0,-1):
    print(""*(n-i),"A"*i)    
    
   