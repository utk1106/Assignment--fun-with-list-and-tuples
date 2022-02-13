#!/usr/bin/env python
# coding: utf-8

# Q Write a Python program to get a list, sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples

# In[7]:


Tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list1 = []
list2 = []

for t in Tuple:
    list1.append(t[1],)
list1.sort()
#print(list1)

for a in list1:
    for b in Tuple:
        if a == int(b[1],):
            list2.append(b)
print(list2)


# In[ ]:




