LAGRANGE’S INTERPOLATION
//Code 1:
def lagrange_interpolation(x,y,xp):
    """
    x:list of x data points
    y:list of corresponding y data points
    xp:value at which interpolation is required
    """
    n=len(x)
    yp=0
    
    for i in range(n):
        p=1
        for j in range(n):
            if i!=j:
                p*=(xp-x[j])/(x[i]-x[j])
        yp+=p*y[i]

    return yp


#-------INPUT SECTION--------

#Enter x and y values
x=list(map(float,input("Enter x values separated by space:").split()))
y=list(map(float,input("Enter y values separated by space:").split()))

if len(x)!=len(y):
    print("Error:x and y must have same number of elements!")
else:
    xp=float(input("Enter the value of x at which y is to be interpolated:"))
    yp=lagrange_interpolation(x,y,xp)
    print(f"Interpolated value at x={xp} is y ={yp}")
