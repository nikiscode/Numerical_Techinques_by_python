



FORWARD_BACKWARD_CENTRAL_DIFFERENCE
//Code 1:
def forward_delta(x,y,h):
    print("\nForward Difference(Δy):")
    for i in range(len(x)-1):
        delta_y=y[i+1]-y[i]
        dy_dx=delta_y/h
        print(f"Δy at x={x[i]}→{delta_y:.6f},f'({x[i]})={dy_dx:.6f}") 
def backward_delta(x,y,h):
    print("\nBackward Difference(∇y):")
    for i in range (1,len(x)):
        nabla_y=y[i]-y[i-1]
        dy_dx=nabla_y/h
        print(f"∇y at x ={x[i]}→{nabla_y:.6f},f'({x[i]})={dy_dx:.6f}")
def central_delta(x,y,h):
    print("\n Central Difference(δy):")
    for i in range (1,len(x)-1): 
        delta_c=(y[i+1]-y[i-1])/2
        dy_dx=delta_c/h
        print(f"δy at x={x[i]}→{delta_c:.6f},f'({x[i]})={dy_dx:.6f}")


n=int(input("Enter number of data points:"))
x=[]
y=[]
print("Enter values of x (equally spaced):")
for i in range(n):
    x.append(float(input(f"x[{i}]=")))
print("Enter values of y:")
for i in range(n):
    y.append(float(input(f"y[{i}]="))) 
if n > 1:
    h=x[1]-x[0]
    forward_delta(x,y,h)
    backward_delta(x,y,h)
    central_delta(x,y,h)
