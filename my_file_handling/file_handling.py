

# ..........................FILE HANDLING......................................


# ....read mode.........

'''file = open('example.txt','r')

content = file.read()
print(content)
file.close()
'''
# ....write mode........

file = open('example2.txt','w')

content = file.write("hey jhon this is viplove on board, where are you")
print(content)
file.close()   

# ...append mode......
file = open('example2.txt','a')

content = file.write("\nyaa i am on the way ")
print(content)
file.close()   