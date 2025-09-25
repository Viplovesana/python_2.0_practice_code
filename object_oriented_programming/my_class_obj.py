

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

'''class Student:
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
print(s1.average())'''


'''class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.mymark = marks

    def average(self):
        sum = 0 
        for i  in self.mymark:
            sum = sum +i
            
        print("hey your average marks is",sum/3)

s1 = Student("viplove",[90,60,70])
print(s1.name,s1.mymark)
s1.average()'''



# create account class with 2 attributes balance and account n0 create method for debit  credit and printing balance

'''
class Account:
    def __init__(self,balance,accno):
        self.mybalance = balance
        self.myacc = accno
    
    def credit(self,amount):
        self.mybalance = self.mybalance + amount
        print ("your acount is credited",self.mybalance)

    def debit(self,amount):
        self.mybalance = self.mybalance - amount
        print ("your acount is debited",self.mybalance)   

    def totalbalance(self):
        print ("total balance in your acc is ",self.mybalance)             

acc1 = Account(1000,8085)
print(acc1.mybalance,acc1.myacc) 
acc1.credit(1000) 
acc1.debit(200) 
acc1.totalbalance()     
'''


# ....INHERITENCE.............................................

# WHEREEONE CLASS USE THE propertis and methods of another class 

# there are three type of inheritence arw there 
'''
1.single inheritence
2.multi-level inheritence
3.multiple inheritence'''

class Car:
    @staticmethod
    def starts():
        print("car started")
    @staticmethod    
    def stops():
        print("car stops") 

class Car1(Car):
    def __init__(self,name):
        self.name = name        
class Types(Car1):
    def __init__(self,type):
        self.type = type

s1 = Types("electric")
print(s1.stops())
print(s1.starts())
print(s1.stops())


 