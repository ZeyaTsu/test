
def calcul(n):
    while n > 1:
        if n % 2:
            n = 3 * n + 1 
            print(n)
        else:
            n = n//2
            print(n)
            
n = int(input("Number > "))
if n < 1:
    print("Error | N < 1.")
else:
    calcul(n)