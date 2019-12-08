#!/usr/bin/env python
# coding: utf-8

# # Problem Statement: TASK 1

# Q1. Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[5]:


Name = input("Enter Your Name:")
print("Hi, {0}... Welcome !!!".format(Name))

Q2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 
# In[6]:


nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))

Q3.Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. 
# In[1]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


# In[4]:


name_list = []
name = input("Enter your full name: ")
name_list = name.split(" ")
reverse_name = name_list[::-1]
for name in reverse_name:
    print(name, end=" ")


# Q4.Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 

# In[3]:


from math import *
def sphere_vol(radius):
    volume = 4/3 * pi * radius ** 3
    return volume
diameter = eval(input("Enter the diameter of Sphere: "))
rad = diameter/2
vol = sphere_vol(rad)
print(vol)


# # Task 2:

# Q1.Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 

# In[9]:


values = input("Enter some comma seprated numbers : ")
output = values.split(",")
print(output)
print("Type of output is :",type(output))

Q2.Create the below pattern using nested for loop in Python. 
# In[13]:


for i in range(0,5):
    for j in range(0,i+1):
        print("*", end =' ')
    print("\r")
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*", end =' ')
    print("\r")


# Q3.Write a Python program to reverse a word after accepting the input from the user.
# Sample Output: 
#  
# Input word: AcadGild 
#  
# Output: dilGdacA 

# In[19]:


word = input('Enter the word:')
while(len(word)):
    print("Reverse of word:",word[::-1], end='')
    print('')
    break


# Q4.Write a Python Program to print the given string in the format specified in the ​sample output. 
#  WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 

# In[20]:


print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN, !  \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC  \n\t\tand to secure to all its citizens")

