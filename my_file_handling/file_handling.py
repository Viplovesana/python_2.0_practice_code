

# ..........................FILE HANDLING......................................


# ....read mode.........

'''file = open('example.txt','r')

content = file.read()
print(content)
file.close()
'''
# ....write mode........

'''file = open('example2.txt','w')

content = file.write("hey jhon this is viplove on board, ")
print(content)
file.close()   

file = open('example2.txt','w')

content = file.write("where are you jhon, ")
print(content)
file.close() 
'''
# ...append mode......

'''file = open('example2.txt','a')

content = file.write("\nyaa i am on the way ")
print(content)
file.close() 

file = open('example2.txt','a')

content = file.write("\nplease wait ")
print(content)
file.close()  '''

# open with 'with' statement............................
'''
with open('example2.txt','r')as file:
    content=file.read()
    print(content)'''

# tell() and seek() funtion.........................
# TELL()......
with open('example2.txt','r')as file:
    print(file.tell())
    content=file.readline(5)
    print(content)
    print(file.tell())
    content=file.readline(2)
    print(content)
    print(file.tell())
    content=file.readline(4)
    print(content)
    print(file.tell())
# SEEK()....  

with open('example2.txt','r')as file:
    print(file.tell())
    content=file.readline(5)
    print(content)
    print(file.tell())  





