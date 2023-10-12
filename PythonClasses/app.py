# ===================== Starting Python ==============
# print("Hello World !!!");
# print("Hello Guys !!!");

# x = 50
# y = 100
# z = "Sir Hamza Ahmed"

# print(x ,"\n" ,y,"\n" , z )


# print('''My name is Sir  Hamza Ahmed.
# My name is 'Sir Hamza Ahmed'
# My name is Sir  Hamza Ahmed 
# I am teaching Python Programming Language. 
# We all are human beings''')


#  ====================== Variable Names =================

# ======================= Illegal And Legal Variables ===============
xy = 55
# 123 = 55
# na12me = 55
# name12333=65
# $%* = 55
# $%%$^%^544 = 98

# name=65

# first name = "wajid"
# firstname = "usman"
# first_name = "Shafeeq"
# firstNameLastName = "Mushtaq"





# print(firstNameLastName)

# ================================ Data Types ======================
# num1 = 100 #============================= Integer =========================
# print(num1) 


# names = "Faheem" #============================ String ===================
# names12 = "98" 
# print(names12)


# status = False #=========================== Boolean Data Type ===========
# active = "False" # ====================== String Data Types ==========
# print(status)
# print(type(status))
# print(type(active))
#  ======================== List (Array) ========================



# name1 = "Shahzaib"
# name2 = "Shafeeq"
# name3 = "Ali"
# name4 = "Shahid"

# names=["shahzaib","shafeeq",False,"Usman","Ali",89,101,True,[98745621,[456],92365478,9247895],"Usman"]
# print(names[2])
# print(type(names))


# ======================= Tuple ======================
# names1 = ("Shahid","Daniyal","Ali",456)
# print(names1)
# print(type(names1))


#  ========================== Dictionary ==================
#  ====================== BAse on key value pairs ==============
# names123 = {
#     "name1":"Fahad",
#     "age":85,
#     "email":"fahad@gmail.com"
# }

# print(names123["email"])

# =========================== Sets ========================
# name1 = {"Dilshad","Usman",78,False}
# print(type(name1))


# Modify 
# lower upper strip replace split

# txt = "The best things in life are free!"
# print("free" in txt)




#  ================================ String Formatting ================
# a = "Hello H WoRlD!!!"
# print(type(a))
# print(a[:5])
# print(a[6:11])
# print(a[6:])
# print(len(a))

# print(a.upper())
# print(a.lower())
# print(a.replace("H","J"))
# print(a.split(" "))

#  ================================== Concatenation ================ Abbas Khan
# firstName = "Abbas"
# lastName = "Khan"
# age = 23
# completeName = firstName+" "+lastName
# print("My full name is: "+completeName+" I am ",age , " years old !!!")

#  ============================ String Formatting =======================
# firstName = "Sir Hamza"
# age = 23
# voteEligibility = 18
# txt = "My name is Sir Hamza Ahmed and I am {1} years old. Eligibility criteria is {0}"
# print(txt.format(voteEligibility,age))
# print(" My name is: "+firstName+" and I am ",age)


#  ================================== Boolean Operators ============================
# num1 = 100
# num2 = 5
# print(num1 > num2)

#  ======================== Math's Equations Practice ============================
# num1 = 100
# num2 = 40
# add = num1 + num2
# sub = num1-num2
# mul = num1*num2
# div = num1/num2
# print(add,"\n",sub,"\n",mul,"\n",div)
# print(sub)
# print(mul)
# print(div)



# ================================= Mini Project ====================
# ================================= marksheet ====================

# completeName = "Shafeeq Ahmed"
# math = 91
# eng = 80
# com = 55
# urdu = 50
# phy = 89
# totalMarks = 100*5

# obtainedMarks = math+eng+urdu+com+phy
# per = (obtainedMarks*100)/totalMarks

# print("My name is",completeName)

# print("My Obtainded Marks is: ",obtainedMarks)
# print("My Percentage is: ",per)



#  ====================== List (Array) ==========================
# name1 = "Farhan"
# name2 = "Wajid"
# name3 = "Ali"

# print(name1)

# names = ["Farhan","Wajid","Ali","Shahzaib","Daniyal",26,45,"Abbas",False,"Sir Hamza Ahmed"]
# print(len(names))
# print(names[4])
# print(type(names))


# ============================== Python List Slicing ==================
# names = ["Farhan","Wajid","Ali","Shahzaib","Daniyal",26,45,"Abbas",False,"Sir Hamza Ahmed"]
# # print(names[2:8])
# # print(names[:5])
# # print(names[5:])
# names[1:5] = ["Shafeeq","Ahmed"]
# print(names)

# Name:Daniyal
# Age:25
# Email:daniyal@gmail.com
# Active:True
# ================= List (  Mini Project ) ====================================
# names = ["Farhan","Noman","Daniyal","Areeb",["farhan@gmail.com","Noman@gmail.com","Daniyal@gmail.com","areeb@gmail.com"],[25,98,26,20],[False,True],"End !!!"]
# print( "Name:" , names[2],"\n","Age:",names[5][0],"\n","Email:",names[4][2],"\n","Active:",names[6][1] , "\n",names[7] )


# ================== List Method ==============

# names = ["Farhan","Noman","Daniyal","Areeb","Daniyal"]
# num1 = [25,65,98]
# mixList =names+num1
# names.extend(num1)
# print(num1) 
# print(names)
# names.append("Hammad")    #======= add element in last
# print(names)
# names.insert(2,"Abbas")     # add element in particular position
# print(names)
# names.pop(1)             #remove last or in particular position
# print(names)
# names.remove("Daniyal")
# print(names)
# names.clear()
# del names
# print(names)

#  ===================== Tuple ==============
# names = ("Farhan","Abbas","Hamza","Ahmed")
# # print(names[2])
# y = list(names)
# y.remove("Abbas")
# print(y)

# =============== Unpacking Tuples =======================
# fruits = ("Apple","Cherry","Mango","Orange","Banana")
# (green,*orange,yellow) = fruits
# print(orange)


# print(type(y))
# print(len(names))



#  ============================= Sets ====================

# names = {"Farhan","Shafeeq","Usman","Umar","Farhan",544,False,1,True,0}
# print(type(names))
# print(names)
# print(names)
# print(len(names))
# names.add("Shehroz")
# # ======= update , remove ,add =======
# print(names)


#  ================================= Dictionary ===================
# ======== carry key value pairs ===========
# key:value

# ==================== Mini Project ==========

# names={
#     "std1":{
#         "std1Name":"Arbaz",
#         "std1Age":23,
#         "std1email":"std1@gmail.com", 
#     },
#         "std2":{
#         "std2Name":"Shan",
#         "std2Age":28,
#         "std2email":"std2@gmail.com",
#     },
#         "std3":{
#         "std3Name":"Saad",
#         "std3Age":23,
#         "std3Email":"std3@gmail.com",
#         "std3PersonalInfo":{
#             "std3FatherContact":4512125545,
#             "std3Siblings":3,
#             "std3FatherEmail":"father@gmail.com"
#         }
#     }
# }
# ============== Std 1 Name , Std 2 Age, Std 3 Email , Std 3 personal Information Father Contact =============
# print("Std 1 Name:",names["std1"]["std1Name"])
# print("Std 2 Age:",names["std2"]["std2Age"])
# print("Std 3 Email:",names["std3"]["std3Email"])
# print("Std 3 Father Contact:",names["std3"]["std3PersonalInfo"]["std3FatherContact"])




# names["emailId"]="hamza@gmail.com"
# # x = names["emailId"]
# print(names)

#  print(len(names))

# names={
#     "name1":"hamza",
#     "age":23,
#     "email":"abc@gmail.com"
# }
# names["contact"]=2552214545
# # print(names.keys())
# # print(names.values())
# names.pop("age")
# print(names)
# print(names.keys())

# # print(len(names))

# ========================= if else ===============


# > < == >=  <=

# a = int(input())
# print(a)


# a = 100 
# b=100
# if a < b:
#     print("a is less than b")
# elif a==b:
#     print("a is  equals to b")
# else:
#     print("a is greter than b")    

# =============== logical operator ========= and or not ===========
# define physics  and its types 



# define physics  OR  its types 


# a = 55



# if a > 1 or a < 0:
#     print("the value is mid between 1 to 10")
# elif a > 10 and a < 20:
#     print("the value is mid between 10 to 20")
# elif a > 21 and a < 30:
#     print("the value is mid between 21 to 30")
# else:
#     print("The number is greater than 30")
    
    
# ============================ Mini Project ========================

# math = int(input("Enter your Math Marks? \n")) 
# physics = int(input("Enter your Physics Marks? \n")) 
# urdu = int(input("Enter your Urdu Marks? \n")) 
# english = int(input("Enter your English Marks? \n")) 
# computer = int(input("Enter your Computer Marks? \n")) 

# obtainedMarks = math+physics+urdu+english+computer
# totalMarks = 100*5    
# per = (obtainedMarks*100)/totalMarks

# if per>=80 and per<=100:
#     print("Your Percentagee is: ",per,"\n","Your Grade is A+")
# elif per>=70 and per <80:
#     print("Your Percentagee is: ",per,"\n","Your Grade is A")
# elif per >=60 and per<70:
#     print("Your Percentagee is: ",per,"\n","Your Grade is B")
# elif per >= 50 and per<60:
#     print("Your Percentagee is: ",per,"\n","Your Grade is C")
# elif per >=40 and per<50:
#     print("Your Percentagee is: ",per,"\n","Your Grade is D")
# elif per>=33 and per <40:
#     print("Your Percentagee is: ",per,"\n","Your Grade is E")
# elif per>=0 and per<33:
#     print("Your Percentagee is: ",per,"\n","Your Grade is F and You are Fail")
# else:
#     print("Your Percentagee is: ",per,"\n","You entered Invalid Marks !!! Stop !!! Try again")
  
        
 # ======================== Loop ======================
#  repeated, itertaion

#  ======== For , While ==============
# inititialization
# for/while condition
# print()
# increment / decrement

# ===================== While =============

# i = 10
# while i>=1:
#     print(i)
#     i-=1
    
    


# =============== While with condition ===============
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     break
#   print(i)

    
    
    
# ================== For Loop =====================

# for x in range(1,10,2):
#     print(x)



# names = ["Arbaz","Zaki","Chris","Charles","Haroon"]
# for x in names:
#     print(x)
#     if x == "Chris":
#         print("Chris name is missing")
     

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])





# ==================== Functions ======================


# === there are two typs of functions 1) Built in/by default  function 2) Customized Function
# print() .ccopy,.update, .clear , .insert()

# # ================== customizd function ================
# def addd(a,b):
#     c = a+b
#     print(c)


# addd(100,500)
# addd(100,100)
# addd(50,500)


# def myfunction(fname,lastname):
#     print("My first name is: ",fname,"My last name is: ",lastname)

# myfunction("Sir Hamza","Ahmed")


# ======== OOP ===== Object Oriented Programming ===============
#  There are 4 main pillars in OOP
# 1)Inheritance / Classees and Objects
# 2)Polymorphism
# 3)Encapsulation
# 4)Abstraction





# ======================= Inheritance / classes and Object ========================
# class Person:
#     pass
    
# class Person():
#     x = 50
#     y = 100
#     c = x+y
 
# p1 = Person() #=========================== Object Constructor ==========   
# print(p1.c)
    

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age = age
        
#     def myfunc(abc):
#         print("My name is :",abc.fname,"I am :",abc.age)
        
    # def __str__(self):
    #     return f"{self.fname} {self.lname} {self.age}"
        
# p1 = Person("Sir Hamza ","Ahmed",23)
# p1.myfunc()











# ====================== Iterators and Next  ======================
# names = ["Amin","Farhan","Shahzaib","Hamza","Ahmed"]
# for x in names:
#     print("My name is: ",x)


# names = ["Amin","Farhan","Shahzaib","Hamza","Ahmed"]
# y = iter(names)


# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# abc = "Sir Hamza Ahmed"
# xyz = iter(abc)
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))
# print(next(xyz))


# =============================== Modules ======================
# modules is same as cod of libraray
#  there are two types of module 
# 1) built in modules
# 2) customized module

# import mymodule as A


# A.greeting("Sir Hamza Ahmed")


# abc = A.person1["email"]
# print(abc)

# ======================== Built In Modules =============
# import platform
# import datetime
# import math


# c1 = math.ceil(99.01)
# f1 = math.floor(99.999)
# srt = math.sqrt(64)


# print(srt)


# print(c1)
# print(f1)



# y = datetime.datetime.now()
# print(y)
# x = platform.system()
# print(x)



# ========================= Scope ============================
# ===== Global Variable Dec/Init ========
# x = 55

# def myfunc():
#     global x
#     x = "Sir Hamza Ahmed !!!"
    
#     def innersidefunc():
#         print(x)
        
#     innersidefunc()
    
   


# myfunc();

# print(x)

# ================== Regular Expression ( RegEx ) =======


import re
#Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"


# x = re.search("Germony", txt)
# if x:
#     print("Yes Good")
# else:
#     print("No, Not Good")



# txt = "The rain in Spain"

# x = re.findall("ai", txt)
# x = re.split("\s",txt)
# x = re.sub("\s", "Sir Hamza Ahmed", txt)

# print(x)



# ======================  JSON  ===========
# ========================= JavaScript Object Notation ===================
# ============= Practcial work on framwork / Project =================



# ==================== User Input ===============

# name1 = input("Enter Your Name ?\n")
# print("My name is:",name1)

# num1 = int(input("Enter Your first Number ? \n"))
# num2 = int(input("Enter Your second Number ? \n"))
# num3 = num1+num2
# print("The Addition result is:",num3)

# ================== PIP ===================
# ========= Python Intsll Package ==========



# x = re.findall("Portugal", txt)
# x = re.split("\s", txt)
# x = re.split("\s", txt, 1)

# print(x)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)





# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()




 
    
    
    
    
    
    
    






    
    
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")





#  ========= problem solving language =========
# ======== Frameworks ================
# framework is a tool=====

# ==== Django , Flask , numpy 











