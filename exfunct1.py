#!/bin/python3

def highest_even(li):
    even_numbers=[]
    for i in li:
        if i%2 == 0:
            even_numbers.append(i)
    return(max(even_numbers))



print(highest_even([10,2,3,4,8,11,10000,10003]))
