'''
Created on Jul 1, 2014

@author: viejoemer
'''
############################################################
#Howto remove an arbitrary element from a dict in python?

#Creating a dict with data

d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }

print(d)

# Removing an "arbitrary" element means that the function can remove whatever 
# item it likes. That doesn't mean that it has to be especially random about it.

d.popitem()

print(d)

print(d)