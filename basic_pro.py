#https://www.geeksforgeeks.org/python-programming-examples/

#Python Program for factorial of a number

#3!= 3*2*1

# def factorial(n):
#     return 1 if(n==0 or n==1) else n*factorial(n-1)

# print(factorial(3))

#-------------------------------

#prime number

# num=5

# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print('prime number')

#-------------------------------------

#palindrome string

# name="madam"
# name = input("enter the value: ")
# reverse =name[::-1]

# if(name==reverse):
#     print("palindrome")
# else:
#     print("not palindrome")

#palindrome number

num =1521

temp = num
reverse =0

while(num>0):
    dig = num%10
    reverse = reverse*10 +dig
    num = num//10

if temp == reverse:
    print("palindrome")
else:
    print("not palindrome")






#-----------------------------------


# name = input("enter the value: ")
# reverse =name[::-1]
# print(reverse)


