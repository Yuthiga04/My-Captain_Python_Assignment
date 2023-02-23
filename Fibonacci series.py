# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:55:06 2023

@author: 65820
"""

a=int(input('Enter a number:'))
s1,s2=0,1
terms=0
print("Fibonacci series:")
while terms<a:
    print(s1)
    c=s1+s2
    s1=s2
    s2=c
    terms=terms+1