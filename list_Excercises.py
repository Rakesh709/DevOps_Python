#https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/

#Python program to interchange first and last elements in a list



# def swapList(newList):
#     size= len(newList)
#     # print(size)
#     temp= newList[0]
#     newList[0]=newList[size-1]
#     newList[size-1]=temp
#     return newList


# print(swapList([1,2,3,4]))

# def swaplist(newList):
#     newList[0],newList[-1]=newList[-1],newList[0]

#     return newList

# print(swaplist([1,2,3,4]))


#-----------------------------------------------------------------------------------

#Python Program to Swap Two Elements in a List
#not getting 


#-------------------------------------------
#How To Find the Length of a List in Python

# def lenght_Finder(arr):
#     n= len(arr)
#     return n

# print(lenght_Finder([1,2,3,4,5]))


# def length_finder(arr):
#     count=0
#     for i in arr:
#         count+=1
#     return count
    
# print(length_finder([1,2,3,4,5]))


#-------------------------------------------------
#Find Maximum of two numbers in Python

# def max_finder(num1,num2):
#     if num1>num2:
#         return "num1 is bigger"
#     else:
#         return "num2 is bigger"

# print(max_finder(-9,-6))

#-------------------------------------------------

#reverse of list

# list = [4, 5, 6, 7, 8, 9]

# print(list[::-1])
# new_list= list.reverse()
# print(list)


#sume od element

# elem = [1,2,3]
# product=1
# for i in elem:
#     product*=i
# print(product)


#-------------------------------------------------

#smallest number in a list

# elem = [11,2,3]

# elem.sort()
# print(elem[0])

# small= elem[0]

# for i in range(len(elem)):
#     if elem[i] <small:
#         small=elem[i]
# print(small)


#Find Largest Number in a List

elem = [11,2,3]

# elem.sort()
# print(elem[-1])


