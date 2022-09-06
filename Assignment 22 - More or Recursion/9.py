"""Write a recursive python function to print octal of a given decimal number."""
def dec_to_Oct(decimal):
    if(decimal > 0):
        dec_to_Oct((int)(decimal/8))
        print(decimal%8, end='')
        
decimal = int(input("Enter a decimal number: "))
print("Octal: ", end='')
dec_to_Oct(decimal)