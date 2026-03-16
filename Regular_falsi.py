##Secant_Method :
//Code2:
import math
func = input("Enter the function f(x): ")
def f(x):
    return eval(func, {"x": x, "math": math})
x0 = float(input("Enter first initial guess x0: "))
x1 = float(input("Enter second initial guess x1: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Enter maximum number of iterations: "))
print("\nIter\t x0\t\t x1\t\t x2\t\t f(x2)")
for i in range(1, max_iter + 1):
    if f(x1) - f(x0) == 0:
        print("Division by zero error.")
        break
   x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(x2,6), "\t", round(f(x2),6))
    if abs(x2 - x1) < tol:
        print("\nRoot =", round(x2,6))
        break
    x0 = x1
    x1 = x2
else:
    print("\nRoot after", max_iter, "iterations =", round(x2,6))

