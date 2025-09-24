

'''class Student:
    print("viplove")
Student()    '''

'''class Student:

    def __init__(self):
        print("this is my default constructor")
        
    def __init__(self,fullname,myage):
       self.name = fullname
       self.age = myage
      
s1 = Student("viplove sana",24) 
print(s1.name,s1.age)

s2 =Student("piyush bhai",22)
print(s2.name,s2.age)'''

'''
class Student:
    def __init__(self,fullname,myage):
        self.name = fullname
        self.age = myage

    def say_hello(self):
        print("hello",self.name)

    def say_bye(self):
        return self.name     

s1 = Student("viplove",24)
print (s1.name,s1.age)

s1.say_hello()
print(s1.say_bye())'''


# create student class thats take name & marks of three subjects as argument in constructor then crete a method to print the average..

class Student:
    def __init__(self,fullname,mark1,mark2,mark3):
        self.name = fullname
        self.markone = mark1
        self.marktwo = mark2
        self.markthree = mark3

    def average(self):
        print("average marks of",self.name,"is :-")
        return (self.markone + self.marktwo + self.markthree )//3


s1 = Student("viplove",90,60,70)
print(s1.name,s1.markone,s1.marktwo,s1.markthree)
print(s1.average())





 