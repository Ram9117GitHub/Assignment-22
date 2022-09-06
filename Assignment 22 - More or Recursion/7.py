"""Write a recursive python function to calculate sum of the digits of a given number ."""
def digits(n):
    if n==0:
        return 0
    return n%10 +digits(n//10)
num = int(input("Enetr a number:") )
di = digits(num)
print("The sum sum of digits is ",di)
""""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Enetr a number:12345
The sum sum of digits is  15
"""