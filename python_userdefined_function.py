##print("hello")
##print("welcome to my programming")

##def My_Fun():#function definition without argument or signature or parameter
##    print("hello")
##    print("welcome to my programming")
##    
##My_Fun()#function calling
##
##def My_Fun(name):#function definition with argument or signature or parameter
##    print("hello",name)
##    print("welcome to my programming")
##
##My_Fun("dhoni")
##My_Fun("kholi")
##My_Fun(4)#function calling


##def My_Fun(name):#function definition with argument or signature or parameter
##        if isinstance(name,str):#to make sure that string is entered
##            print("hello",name)
##            print("welcome to my programming")
##
##My_Fun("dhoni")
##My_Fun("kholi")
##My_Fun(4)#function calling


##def My_Fun(name,country):#function definition with argument or signature or parameter
##        if isinstance(name,str) and isinstance(country,str):#to make sure that string is entered
##            print("hello",name,"from",country)
##            print("welcome to my programming")
##
##My_Fun("dhoni","chennai")
##My_Fun("kholi","banglore")
##My_Fun("kapil","delhi")#function calling


##def My_Fun(name,country):#function definition with argument or signature or parameter
##        if isinstance(name,str):
##            if isinstance(country,str):
##                print("hello",name,"from",country)
##                print("welcome to my programming")
##
##My_Fun("dhoni","chennai")
##My_Fun("kholi","banglore")
##My_Fun("kapil","delhi")#function calling

##
##def My_Fun(name,country):#function definition with argument or signature or parameter
##        if isinstance(name,str):
##            if isinstance(country,str):
##                print("hello",name,"from",country)
##                print("welcome to my programming")
##
##My_Fun(country="dhoni",name="chennai")
##My_Fun(name="kholi",country="banglore")
##My_Fun("kapil","delhi")

##
##def My_Fun(name,country="india"):#function definition with default argument or signature or parameter
##        if isinstance(name,str):
##            if isinstance(country,str):
##                print("hello",name,"from",country)
##                print("welcome to my programming")
##
##My_Fun("dhoni")#function calling with default argument
##My_Fun("kholi","banglore") 
##My_Fun("sunny")
##My_Fun("kapil","delhi")


##def My_Fun(name,country=None):#function definition with default argument or signature or parameter
##    print("hello",name,"from",country)
##    print("welcome to my programming")
##
##My_Fun("dhoni")
##My_Fun("kholi","banglore")
##My_Fun("sunny")
##My_Fun("kapil","delhi")


##
##def My_Fun(name="sachin",country=None):#function definition with argument or signature or parameter
##    
##                print("hello",name,"from",country)
##                print("welcome to my programming")
##
##My_Fun()
##My_Fun("kholi")
##My_Fun("kapil","delhi")
##
##
##def My_Fun(name="sachin",country):#function definition with argument or signature or parameter
##      
##                print("hello",name,"from",country)
##                print("welcome to my programming")
##
##My_Fun()  #will throw error non default argument follows the default argument

##def Student_Passed(*name):
##    print(name)
##
##Student_Passed("dhoni")
##Student_Passed("kohli","sachin")
#args means it can take any number of arguments
#output will be in the form of tuple

##def Student_Passed(**name):
##    print(name)
##
##Student_Passed("dhoni")
##Student_Passed("kohli",age=33)

##def Student_Mark(eng,math,student_name):
##    total = eng + math
##    return
##print(Student_Mark(40,50,"dhoni"))



##def Student_Mark(eng,math,student_name):
##    total = eng + math
##    return
##output=Student_Mark(40,50,"dhoni")
##print(output)

##def Student_Mark(eng,math,student_name):
##    total = eng + math
##    
##    return total
##    print("welcome")
##    
##output=Student_Mark(40,50,"dhoni")
##print(output)

##def Student_Mark(eng,math,student_name):
##    total = eng + math
##    
##    return total,student_name
##    print("welcome")
##    
##output,output1=Student_Mark(40,50,"dhoni")
##print(output)
##print(output1)

#scoping
##var=100 #outside variable(Global)
##def fun():
##    var =10 #local variable
##    print(var)
##
##print(var)
##fun()
##print(var)
##
##
##var=100 #outside variable(Global)
##def fun():
##    global var
##    var =10 #local variable
##    print(var)
##
##print(var)
##fun()
##print(var)

##
##count=0
##def fun():
##    global count
##    print("hello",count)
##    count=count+1
##    fun()
##    
##
##fun()

##
##count=0
##def fun():
##    global count
##    print("hello",count)
##    count=count+1
##    if count == 101:
##        return
##    fun() 
##
##fun()



count=0
def fun():
    global count
    print("hello",count)
    count=count+1
    while count <101:
    fun()
    
fun()
##
##
##count=0
##def fun():
##    global count
##    print("hello",count)
##    count=count+1
##    if count <101:
##    fun()
##    
##
##fun()












