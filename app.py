# print("Hello World");

# age=20
# price = 19.96
# first_name='rakesh'
# is_online= False
# print(age)

# patient_name= "john smith"
# age=20

# --------

# name=input("what is your name ")
# print("hello " + name)

#-------------------

# birth_year = input("Enter your birth year: ")
# age = 2020 - int(birth_year)
# print(age)

# num1= float(input("first: "))
# num2= float(input("second: "))
# print(num1+num2)

#-------------------
#string

# course = "Python for bignners"
# print(course.upper())
# print(course.find('y')) #return the first occuring index 
# print(course.replace("for","4"))
# print("Python" in course)

#----------------
#Arithmatic operator

#print(10/3) 
#3.3333333333333335
#print(10//3)
#3
#print(10%3) #reminder 1

# print(10**3)

#ogumented assigned operator

# x=3
# # x=x+3
# x+=3  # agumented assigned operator
# print(x)

#----------------------

#operator precedence

#bodmas
# x=10+3*2
# print(x)

#------------------
#comparision operator

# x=3>2
# x=3==2
# x= 3!=2
# print(x)

# >
# >=
# <
# <=
# ==
# !=

#--------------------------
#logical operator

# price=25
# print(price>10 and price<30)
# True

# price=5
# print(price>10 or price<30)
# True

# price =5
# print(not price>10)
#True


# and (both)
# or (at least one)
# not (opposite)

#----------------------
#if statement

# temp=5

# if(temp>30):
#     print("It's hot outside")
# elif(temp>20):
#     print("It's warm outside")
# elif(temp>10):
#     print("It's mild outside")
# else:
#     print("temp is cold")

#------------------------------------

#exercise

# weight = float(input("Enter your weight: "))
# weight_in_kg_or_lbs= input("(k)g or(L)bs: ")

# if(weight_in_kg_or_lbs == "K" and "k"):
#     print("Weight in Kg: " + weight_in_kg_or_lbs)

# weight= int(input("weight: "))
# unit = input("(k)g or (L)bs: ")

# if unit.upper() == 'K':
#     converted = weight/ 0.45
#     print("weight in lbs: "+ str(converted))
# else:
#     converted = weight * 0.45
#     print("weight in kg: " + str(converted))


#--------------------------
#while

# i=1
# while i<=5:
#     print(i)
#     i+=1


# i=1
# while i<=5:
#     print(i*"*")
#     i+=1

#===============
#list

# 1- number
# 1.1 - float
# True - boolen
# "a" - string 

# primative datatype or basic datatype

# name = ["john","bob","Mosh"]
# # name[0]="joh"
# # print(name)
# # print(name[0])
# # print(name[-1])

# print(name[0:2])


#list method

# numbers=[1,2,3,4,5]
# numbers.append(6)
# numbers.insert(0,-1) #insert(index,value) to insert in between
# numbers.remove(3)
# print(1 in numbers)
# print(numbers)
# print(len(numbers))

#---------------------
#for Loop

numbers=[1,2,3,4,5]

# for items in numbers:
#     print(items)

# i=0
# while i <len(numbers):
#     print(numbers[i])
#     i=i+1

#-------------------
#range() function

# numbers=range(5)
# print(numbers)

# numbers= range(1,10,2)

# for number in numbers:
#     print(number)

#------------------------

#tuples

# numbers =(1,2,3)
