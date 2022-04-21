#python is unstructured programming
#python can be made as structured programming if it follows "class" principles
#class is collection of objest
#object is real world entity
#class is kind of templatee or wrapper to hold things
#object is anything which takes memory
#class is mainly to give the property of inheritance or extensibility

##var="dhoni"
##print(var)
##
##def fun():
##    print("welcome")
##
##fun()

##class My_Class:
##    var="dhoni"
##
##    def fun():
##        print("welcome")
##print(My_Class.var)
##My_Class.fun()

##class My_Class:
##    var="dhoni"
##
##    def fun():
##        print("welcome")
##My = My_Class
##print(My.var)
##My.fun()
#My is called object reference of the "My_Class"
#class without constructor
##
##class My_Class:
##
##
##    def fun(name,age):
##        print("welcome")
##
##    def new(name):
##        print("hello")
##
##My = My_Class
##My.fun("dhoni",33)
##My.new("dhoni")

##
##
##class My_Class:
##    def __init__(lisha,name,age):
##
##        lisha.name = name
##        lisha.age = age
##
##
##    def new(lisha):
##        print(lisha.name)
##
##    def fun(lisha):
##        print(lisha.name,lisha.age)
##
##My = My_Class("dhoni",33)
###My_Class is called as constructor class
###My is called as object reference with single instant memory(single instant memory)
###My_Class() will have one hidden object inside
###whenever you create constructor , an attribute called __intit__ is created automatically
###attribute or magic method or dunder method is anything that contain double underscore on either side
###lisha is similar to My
###My is object reference for external class
###self is the object reference for internal class
##My.fun()
##My.new()


#7th of April
##
##class My_Class:
##    """Author ka naam :- Kapil Vats"""
##
##    def __init__(self,name,age):
##        self.age=age
##        self.name=name
##        
##    def new(self,country):
##        print(self.age,country)
##
##    def fun(self):
##        print(self.age,self.name)
##
##my=My_Class("dhoni",33)
##my.fun()
##my.new("india")
##print(my.__doc__)#print the document string  author ka naam


#https://www.techbeamers.com/python-class

##class My_Class:
##
##    def fun(self):
##        print("welcomr to python")
##my = My_Class()
##my.fun()


##class My_Class(object):  # line number 100 and 108 is same
##
##    def fun(self):
##        print("welcomr to python")
##my = My_Class()
##my.fun()

class My_Class(object):

    def __init__(self):
        print("hello")

    def fun(self):
        print("welcome to python")
my = My_Class()
my.fun()
