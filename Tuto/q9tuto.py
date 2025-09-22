#Work done
def Work_done (F,D):
    return (F*D)
f= float(input("Enter the value of Force acting over a distance d in Newton: "))
d = float (input("Enter the value of distance d in meter: "))
W= Work_done (f,d)
print ("The work done by force over a distance d in the direction of it is ", W, 
        " Joule")

