# Heat transferred
def Heat_tran (m,c,t):
     return (m*c*t)
M = float(input ("Enter the mass of object in Kg: "))
C = float(input("Enter the specific heat in J/Kg.K: "))
T= float (input("Enter the change in temperature in Kelvin: "))
H= Heat_tran (M,C,T)
print ("The heat transferred to an object is" , H , " Joule")

