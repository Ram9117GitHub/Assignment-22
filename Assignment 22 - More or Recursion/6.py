"""Write a recursive python function to calculate the factorial of a number."""
def factoral(n):
    if n==0:
        return 1
    return n*factoral(n-1)
num = int(input("Enter a Natural number:"))
fac = factoral(num)
print("Factoral number = ",fac)
