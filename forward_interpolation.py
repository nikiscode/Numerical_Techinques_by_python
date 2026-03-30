n = int(input("Enter number of data points:"))
x = []
y = []

print("Enter x values:")
for i in range(n):
    x.append(float(input()))

print("Enter y values:")
for i in range(n):   # fixed missing 'in'
    y.append(float(input()))

diff = [y.copy()]

for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i-1][j+1] - diff[i-1][j])
    diff.append(temp)

xp = float(input("Enter value of x to find y:"))  # fixed missing bracket

h = x[1] - x[0]
p = (xp - x[0]) / h

yp = y[0]
fact = 1
p_term = 1   # fixed variable name consistency

for i in range(1, n):   # fixed loop syntax
    p_term = p_term * (p - i + 1)   # fixed variable name
    fact = fact * i
    yp = yp + (p_term * diff[i][0] / fact)   # fixed bracket

print("Interpolated value=", yp)
