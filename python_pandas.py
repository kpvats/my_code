import csv
##with open("python.csv","w",newline="") as file_obj: #newline is an attribute to remove the space between each row 
##
##    file_obj_csv= csv.writer(file_obj) #we have converted file object into csv file obejct
##
##    file_obj_csv.writerow(["name","age","runs"])
##    file_obj_csv.writerows([["dhoni","33","99"],["a","44","55"],["kapil","27","99"]])

##with open("python1.csv","w",newline="") as file_obj:
##
##    file_obj_csv= csv.DictWriter(file_obj,["name","age","runs"]) # we have converted file object into dictionary object
##
##    file_obj_csv.writeheader()
##    file_obj_csv.writerows([{"name":"kapil","age":27,"runs":89},{"name":"kapil vats","age":26,"runs":87}])
    
import pandas
my_input=[["name","age","runs"],["kapil",27,99],["vats",28,101]]
my_final_input=pandas.DataFrame(my_input)
print(my_final_input)

my_final_input.to_csv("mydata.csv",index=None)
#DataFrame(two dimension),Series(single dimesion),Panles(3 D)
