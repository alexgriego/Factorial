n = int (input("Digite numero: "))
def factorial(n):
    if (n==0):
        return 1
    else:
        return n * factorial(n-1)
print("El factorial de : " + str(n) + ": es: " + str(factorial(n)))