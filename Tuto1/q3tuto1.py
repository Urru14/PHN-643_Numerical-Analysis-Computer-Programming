# Q3
def st_line(x1,y1,x2,y2,x):
    return y1 + ((y2-y1)/x2-x1)*(x-x1)

print("This program return the value of y i.e f(x) when two coordinates of a line a given")
x1=float(input("Enetr the x1 value: "))
y1=float(input("Enetr the y1 value: "))
x2=float(input("Enetr the x2 value: "))
y2=float(input("Enetr the y2 value: "))
x=float(input("Enetr the x value correponding to which you want y value: "))
y= st_line(x1, y1, x2, y2, x)
z= round(y,2)
print ("The value of y corresponding to the given x value if a line is considered ", z)

