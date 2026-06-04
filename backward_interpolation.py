##backward interpolation 
n = int(input("Enter number of data points:"))
x = []
y = []
print("Enter x values:")
for i in range(n):
    x.append(float(input()))
print("Enter y values:")
for i in range(n):   
    y.append(float(input()))
diff = [y.copy()]
for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i-1][j+1] - diff[i-1][j])
    diff.append(temp)
xp = float(input("Enter value of x to find y:"))  
h = x[1] - x[0]
p = (xp - x[n-1]) / h
yp = y[n-1]
fact = 1
p_term = 1   
for i in range(1, n):   
    p_term = p_term * (p + i - 1)   
    fact = fact * i
    yp = yp + (p_term * diff[i][-1] / fact)   
print("Interpolated value=", yp)
