# función iterativa

def fact_i(n):
    
    factorial = 1
    
    for i in range(n):
        
        factorial *= (i + 1)
    
    return factorial

entero = int(input("Introduce un número entero para calcular su factorial: "))

print("Su número factorial es", fact_i(entero))


# función recursiva

def fact_r(n):
    
    enteroOK = True
    
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        enteroOK = False
    else:
        return n * fact_r(n-1)

n = int(input("Introduce un número entero para calcular su factorial: "))
enteroOK = fact_r(n)

if enteroOK:
    print("Su número factorial es",fact_r(n))
else:
    print("Debes introducir un número entero mayor o igual a cero.")
    
