##var={}
##print(var)
##print(type(var))
##
##
##var={"dhoni",33}
##print(var)
##print(type(var)) # will give output set data type


##var={"name":"dhoni","age":33}
##print(var)
##print(type(var))


##
##var={"name":"dhoni","age":33}
##print(var[0]) #no index based direct data retrival in dictionary

#in dictionary datas are manipulated or used via key
# dictionary is called key value pair
#because each data we use needs to be stored with specific key
#storing data with key is generally called "Hashing" or Hashtable

##var={"name":"dhoni","age":33}
##print(var["age"])
##
##
##var={"name":"dhoni","age":33}
##var["name"] ="kholi"
##print(var)
###dictionary is mutable type

##
##
##var={"name":"dhoni","age":33,"name":"arjun"}
##print(var)

#keys are unique
#dictionary is called as "Unordered collection"

##var={"name":"dhoni",9:33,98.9:"arjun",("a","B"):"veena",True:"rahul"}
##var["name"]="kholi"  #only immutable data can be formed as key like tuple in ("a","B")
##print(var)
##
##
##var={"name":"dhoni"}
##var["country"] ="india"
##print(var)
##
##var={"name":"dhoni","team":"csk"}
##output=var["team"]
##print(output)
 


##var={"name":"dhoni","team":"csk"}
##var1={"age":33}
##output= var+var1  #this is not possible in dictionary
##print(output)


##
##var={"name":"dhoni","team":"csk"}
##var1={"age":33}
##var2={"lan":"emg"}
##output= {**var,**var1,**var2}  #syntax to concatenate dictionary
##print(output)
##
##
##var={"name":["dhoni","kholi"],"team":("csk","rcb"),"sports":{"cricket":["sachin","Dravid"]}}
##print(var)
##
##
##var={"name":["dhoni","kholi"],"team":("csk","rcb"),"sports":{"cricket":["sachin","Dravid"]}}
##output=var["team"][1]
##print(output)
##
##
##
##
##var={"name":["dhoni","kholi"],"team":("csk","rcb"),"sports":{"cricket":["sachin","Dravid"]}}
##var["name"][1]="rohit"
##print(var)



##var={"name":["dhoni","kholi"],"team":("csk","rcb"),"sports":{"cricket":["sachin","Dravid"]}}
##output=var["country"]
##print(output)
##print("welcome")    #will throww error

##
##var={"name":["dhoni","kholi"],"team":("csk","rcb"),"sports":{"cricket":["sachin","Dravid"]}}
##output=var.get("country")
##print(output)   #will print none because python didint find country key
##print("welcome") #welcome will not be printed 



var={"name":["dhoni","kholi"],"team":("csk","rcb"),"sports":{"cricket":["sachin","Dravid"]}}
output=var.get("country","sorry key not found")
print(output)  #will print none and welcome will be printed 
print("welcome")










