"""Write a recursive python function to calculate sum of first N even natural numbers."""
def evenN(n):
    if n==0:
        return 0
    return 2*n + evenN(n-1)
num = int(input("Enter a Natural number :"))
s = evenN(num)
print("The sum of even is ",s)