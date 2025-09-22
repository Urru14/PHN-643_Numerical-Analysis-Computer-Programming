def Electric_force ( q1,q2,r):
    k= 8.98e10
    return (k*q1*q2)/r**2
Q1= float(input("Enter value of Charge 1 (in Coulomb): "))
Q2= float (input( "Enter value of Charge 2 (in Coulomb): "))
R= float (input( "Enter the distance between two charges: "))
E= Electric_force ( Q1,Q2,R)
print ("The magnitude of Electric force between two point charges is ", E , " Newton"
        )

