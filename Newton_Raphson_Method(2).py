


import math

# input g(x) from user
g_input = input("Enter the function g(x): ")

# define function g(x)
def g(x):
    return eval(g_input, {"x": x, "math": math})

# input initial guess
x0 = float(input("Enter initial guess x0: "))

# input tolerance
tol = float(input("Enter tolerance: "))

# input maximum number of iterations
max_iter = int(input("Enter maximum number of iterations: "))

print("\nIteration\t x0\t\t x1\t\t |x1-x0|")

# Fixed point iteration
for i in range(1, max_iter + 1):

    x1 = g(x0)
    error = abs(x1 - x0)

    print(f"{i}\t\t{x0:.6f}\t{x1:.6f}\t{error:.6f}")

    if error < tol:
        print("\nRoot found:", round(x1,6))
        break

    x0 = x1

else:
    print("\nMethod did not converge within maximum iterations.")
