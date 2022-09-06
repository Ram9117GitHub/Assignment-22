"""Write a recursive python function to print binary of a given decimal number."""
def binnary(n):
    if n>=1:
        binnary(n//2)
        print(n%2,end="")
num = int(input("Enter a decmial number:"))
bi = binnary(num)