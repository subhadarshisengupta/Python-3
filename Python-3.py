
# coding: utf-8

# In[30]:


## Illustration of built-in reduce() function to add a list of numbers
def addition(a,b):
    return a+b

element_list = [1,2,3,4,5]
print(reduce(addition,element_list,0))


# In[31]:


## Illustration of my own myreduce() function to add a list of numbers
def addition(a,b):
    return a+b

def myreduce(func, element_list):
    if len(element_list)==0:
        return 0
    else:
        result = element_list[0]
        for i in range(1,len(element_list)):
            result=func(result,element_list[i])
        return result

element_list = [1,2,3,4,5]
print(myreduce(addition,element_list))


# In[33]:


## Illustration of my own myfilter() function to print the even numbers from a given list
def check_even(a):
    return a%2==0

def myfilter(func, element_list):
    return [element for element in element_list if func(element)==True]

element_list = [213,343,3264,1124,4678,24,67,97,103,66,8620]
print(myfilter(check_even,element_list))


# In[35]:


## Illustration of built-in filter() function to print the even numbers from a given list
def check_even(a):
    return a%2==0
element_list = [213,343,3264,1124,4678,24,67,97,103,66,8620]
print(list(filter(check_even,element_list)))


# In[41]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print (" ACADGILD can be broken to " + str(alphabet_list))


# In[46]:


inputlist = ['x','y','z']
result = [ item*num for item in inputlist for num in range(1,5)  ]
print("The output is " +   str(result))


# In[47]:


inputlist = ['x','y','z']
result = [ item*num for num in range(1,5) for item in inputlist  ]
print(" The Output is " +   str(result))


# In[48]:


inputlist = [2,3,4]
result = [ [item+num] for item in inputlist for num in range(0,3)]
print("The Output is " +  str(result))


# In[49]:


inputlist = [2,3,4,5]
result = [ [item+num for item in inputlist] for num in range(0,4)  ]
print(" The Output is " +  str(result))


# In[53]:


inputlist=[1,2,3]
result = [ (b,a) for a in inputlist for b in inputlist]
print("The Output is " +  str(result))


# In[61]:


a=[]
n= int(input("Enter the number of words in the list:"))
for x in range(0,n):
    word=input("Enter word" + str(x+1) + ":")
    a.append(word)
max=len(a[0])
LongestWord=a[0]
for i in a:
    if(len(i)>max1):
       max=len(i)
       LongestWord=i
print("The word with the longest length is: ")
print(LongestWord)

