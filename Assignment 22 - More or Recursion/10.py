"""Write a recursive python function to find the Nth term of the Fibonacci series."""
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
num = int(input("Enter a number:"))
fibo_series =[]
for i in range(0,num):
    fibo_series.append(fibonacci(i))
print(fibo_series)
