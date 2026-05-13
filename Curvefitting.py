##curvefitting method 
import numpy as np
def exponential_fit(x,y):
    x=np.array(x,dtype=float)
    y=np.array(y,dtype=float)
if np.any(y<=0):
        print("Error:All y values must be positive for exponential fit.")
        return 
    Y=np.log(y)
    n=len(x)
    Sx=np.sum(x)
    Sy=np.sum(Y)
    Sxx=np.sum(x*x)
    Sxy=np.sum(x*Y)

    b=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
    A=(Sy-b*Sx)/n
    a=np.exp(A)

    print("\nExponential Fit:y=a*e^(bx)")
    print("a=",a)
    print("b=",b)


def geometric_fit(x,y):
    x=np.array(x,dtype=float)
    y=np.array(y,dtype=float)

    if np.any(x<=0) or np.any(y<=0):
        print("Error:All x and y must be positive for geometric fit:")
        return

    X=np.log(x)
    Y=np.log(y)

    n=len(x)
    Sx=np.sum(X)
    Sy=np.sum(Y)
    Sxx=np.sum(X*X)
    Sxy=np.sum(X*Y)

    b=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
    A=(Sy-b*Sx)/n
    a=np.exp(A)

    print("\nGeometric Fit:y=a*x^b")
    print("a=",a)
    print("b=",b)


n=int(input("Enter number of data points:"))
x=list(map(float,input("Enter x values separated by space:").split()))
y=list(map(float,input("Enter y values separated by space:").split()))

if len(x)!=n or len(y)!=n:
    print("Error:Number of inputs does not match n.")
else:
    exponential_fit(x,y)
    geometric_fit(x,y)
