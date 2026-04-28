
##Regular_Falsi:
import math
func = input("Enter the function f(x): ")
def f(x):
    return eval(func)
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
if f(a) * f(b) >= 0:
    print("Invalid interval. f(a) and f(b) must have opposite signs.")
else:
    tol = float(input("Enter tolerance: "))
    max_iter = int(input("Enter number of iterations: "))
    print("\nIter\t a\t\t b\t\t c\t\t f(c)")
    for i in range(1, max_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(c,6), "\t", round(f(c),6))
        if abs(f(c)) < tol:
            print("\nRoot =", round(c,6))
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    else:
        print("\nRoot after", max_iter, "iterations =", round(c,6))


 


