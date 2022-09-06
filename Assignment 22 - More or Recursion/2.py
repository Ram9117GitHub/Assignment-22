"""Write a recursive python function to calculate sum of first N odd natural numbers."""
def oddN(n):
    if n==1:
        return 1
    return ((2*n)-1) + oddN(n-1)
num = int(input("Enter a Natural number :"))
s = oddN(num)
print("The sum of odd  is ",s)
