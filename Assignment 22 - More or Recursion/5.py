"""Write a recursive python function to calculate sum of cubes of first N natural numbers"""
def cubesSum(n):
    if n==1:
        return 1
    return n**3 + cubesSum(n-1)
num = int(input("Enter a Natural number :"))
sum_of_cubes = cubesSum(num)
print("The sum of Cubes is ",sum_of_cubes)