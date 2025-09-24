

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
'''with open('example2.txt','r')as file:
    print(file.tell())
    content=file.readline(5)
    print(content)
    print(file.tell())
    content=file.readline(2)
    print(content)
    print(file.tell())
    content=file.readline(4)
    print(content)
    print(file.tell())'''
# SEEK()....  

'''with open('example2.txt','r')as file:
    print(file.tell())
    file.seek(5)
    print(file.tell())
    file.seek(7)
    print(file.tell())
    data1 = file.readline()
    print(data1)
    file.seek(10)
    print(file.tell())
    data2 = file.readline()
    print(data2)
    file.seek(14)
    print(file.tell())
    data3 = file.readline()
    print(data3)
'''



# ....PICKLING AND UNPICKLING...................


# pickling is serialization process where a python objects convert in a byte sream

import pickle
# data = ["viplove",23,"dewas",]

'''byte = pickle.dumps(data)
print(byte)

py_object = pickle.loads(byte)
print(py_object)'''

data = ["viplove",23,"dewas",]
file = open("rowdata.txt",'wb')
pickle.dump(data,file)
file.close()




 





