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
'''n = int(input("Enter the no :"))

for i in range(0,n + 1):
    print(""*(n-i),"A"*i)

for i in range(n,0,-1):
    print(""*(n-i),"A"*i)  ''' 


#WAP....... 
#        * 
#       ** 
#      *** 
#    **** 
#  ***** 
# ***** 
# **** 
# *** 
# ** 
# * 
'''n = int(input("Enter the num :"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n,0,-1):
    print(""*(n-i)+"*"*i) '''
    
# WAP........
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
'''n = int(input("Enter the num :"))
for i in range(n,0,-1):
    # print(" "*(n-i)+"*"*(2*i-1))
    print(" "*(n-i)+"* "*i)'''

# WAP.........
# 1 2 3 4 5  
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
'''n = int(input("Enter the num :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print() '''   


# WAP...............
# 1    
# 1 2  
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
'''n = int(input("Enter the num :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()  '''  
# WAP.........
# 1 2 3 4 5  
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
'''n = int(input("Enter the num :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print() '''   
# WAP...............
# 1    
# 1 2  
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
'''n = int(input("Enter the num :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print() '''   

# WAP ...
# A B C D E  
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E
'''n = int(input("Enter the num :"))
for i in range(1,n+1):   
    ch = "A"
    for j in range(1,n+1):
        print(ch,end="")
        ch = chr(ord(ch)+1) 
    print()  '''

# WAP...
# 2  
# 2 4 
# 2 4 6 
# 2 4 6 8       
# 2 4 6 8 10
'''n = int(input("Enter the no :"))
for i in range(1,n+1):
    ch = 'A'
    for i in range(1,i+1):
        print(ch,end="")
        ch = chr(ord(ch)+1)
    print()  '''    

#  WAP ......
# 2  
# 2 4 
# 2 4 6 
# 2 4 6 8 
# 2 4 6 8 10 
'''n = int(input("Enter the no :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j,end="")  
    print() '''


# WAP......
# 1  
# 1 3 
# 1 3 5 
# 1 3 5 7 
# 1 3 5 7 9 
'''n = int(input("Enter the no :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end="")  
    print() '''
    

# WAp........
#         1 
#        1 2 
#       1 2 3
#      1 2 3 4
#     1 2 3 4 5 
'''n = int(input("Enter the no :"))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    for j in range (1,i+1):
        print(j,end=" ")   
    print()  '''  



