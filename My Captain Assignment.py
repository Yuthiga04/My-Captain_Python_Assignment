# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:42:40 2023

@author: 65820
"""

f=str(input('Enter a name of the file:'))
x=str(input('Enter the extension of the file:'))
a=f+x
print('The name of the file is',a)
s={".py": 'python', ".doc": 'word',".xls": 'excel',".ppt": 'powerpoint',".jpg": 'photo file',".jpeg": 'image file'}
b=s.keys()
c=s.values()
l1=list(b)
l2=list(c)
for i in range(len(l1)):
    if x==l1[i]:
        print('The extension of the file is',l2[i])