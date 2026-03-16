##bisection method maths practise in pythonS

import math
# input function from user
func = input("Enter function f(x): ")

def f(x):
    return eval(func)

# input interval and tolerance
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
tol = float(input("Enter tolerance: "))

# check validity
if f(a) * f(b) >= 0:
    print("Invalid interval. Root not guaranteed.")
else:
    step = 1
    c = a   # initialize c

    print("\nStep\t a\t\t b\t\t c\t\t f(c)\t\t |b-a|")
    print("----------------------------------------------------------------")

    while abs(b - a) > tol:
        c = (a + b) / 2

        print(step, "\t",
              format(a, ".6f"), "\t",
              format(b, ".6f"), "\t",
              format(c, ".6f"), "\t",
              format(f(c), ".6f"), "\t",
              format(abs(b - a), ".6f"))

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        step += 1

    print("----------------------------------------------------------------")
    print("Approximate root =", format(c, ".6f"))
    print("Number of iterations =", step)
