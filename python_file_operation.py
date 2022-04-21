##file_obj = open("kapil.txt","w") # w is for write
##file_obj.write("india is my country")
##file_obj.close() #very important to close the file

##file_obj = open(r"D:\netzwerk_academy_python\kapil.txt","w") # r is for raw data
##file_obj.write("india is my country")
##file_obj.close()
##
##file_obj=open("kapil.txt","w")
##file_obj.write("python prarthana")
##file_obj.close()


##file_obj=open("kapil.txt","a") #append is for a
##file_obj.write("\n")
##file_obj.write("today is tuesday")
##file_obj.close()

##file_obj=open("kapil.txt","a") #append is for a
##file_obj.write("\n")
##file_content=input("enter the file comtent")
##file_obj.write(file_content)
##file_obj.close()

##file_obj=open("kapilvats.txt","x") #it throws error file already existed
##file_obj.write("\n") #and x is for creating a new file
##file_content=input("enter the file comtent:-")#so i changes file name to kapilvats
##file_obj.write(file_content)#new file is created 
##file_obj.close()

#context manager
#we dont need to close while using the context manager with s the keyword

##with open("kapil.txt","a") as file_obj:
##    file_obj.write('\n')
##    file_content=input("enter the content:-")
##    file_obj.write(file_content)

##with open("kapil.txt","r") as file_obj:
##    file_output=file_obj.read()
##    print(file_output)


##with open("kapil.txt","r") as file_obj:
##    file_output=file_obj.read(5)
##    print(file_output)
##    file_output1=file_obj.read()
##    print(file_output1)

##with open("kapil.txt","r") as file_obj:
##    file_output=file_obj.readline()
##    print(file_output)
##    file_output1=file_obj.readline()
##    print(file_output1)








