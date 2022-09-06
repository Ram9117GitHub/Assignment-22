"""Write a recursive python function to calculate sum of squares of first N natural numbers"""
def squaresSum(n):
    if n==1:
        return 1
    return n**2 +squaresSum(n-1)
num = int(input("Enter a Natural number :"))
Su = squaresSum(num)
print("The sum of Squares is  ",Su)