##newton raphson 
import math
# input function and its derivative
func = input("Enter the function f(x): ")
dfunc = input("Enter the derivative f'(x): ")
# define function
def f(x):
    return eval(func)
def df(x):
    return eval(dfunc)
# input initial guess, tolerance, and maximum iterations
x0 = float(input("Enter initial guess: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Enter maximum number of iterations: "))
print("\nIter\t x0\t\t x1\t\t f(x1)")
# Newton-Raphson iteration
for i in range(1, max_iter + 1):
 if df(x0) == 0:
        print("Derivative is zero. Method fails.")
        break
  x1 = x0 - f(x0) / df(x0)
 print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(f(x1),6))

  # convergence check
    if abs(x1 - x0) < tol:
        print("\nRoot =", round(x1,6))
        break

    x0 = x1

else:
    print("\nMethod did not converge.")

