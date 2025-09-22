#Frequency

def freq (v,w):
    return (v/w)
V = float (input("Enter the speed of sound in m/s: "))
W= float(input("Enter the wavelength of sound in meters: "))
F= freq (V,W)
print ("The frequency of sound is ", F, " hertz.")


