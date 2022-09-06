"""Write a recursive python function to calculate sum of first N natural numbers. """

def SumN(n):
    if n<=1:
        return 1
    return n+SumN(n-1)
num = int(input("Enter a Natural number"))
s = SumN(num)
print("The sum is ",s)