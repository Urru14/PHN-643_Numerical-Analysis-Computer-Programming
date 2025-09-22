import numpy as np
def fact(n):
    gfact = [1]  # Create a new list to store factorials
    
    for i in range(1, n + 1):
        gfact.append(gfact[i - 1] * i)
    return gfact[-1]


def cos_approx(x, N):
    """
    Approximate cos(x) using Taylor series up to N terms.
    """
    sum_cos = 0
    for n in range(0, N + 1):
        term = ((-1)**n) * (x**(2*n)) / (fact(2*n))
        sum_cos += term
    return sum_cos

def sin_approx(x, N):
    """
    Approximate sin(x) using Taylor series up to N terms.
    """
    sum_sin = 0
    for n in range(1, N + 1):
        term = ((-1)**(n + 1)) * (x**(2*n - 1)) / (fact (2*n - 1))
        sum_sin += term
    return sum_sin

print("_"*60)

x_values = [0, 1/4, 1/2, 3/4]
N_values = [5, 10, 20]
for x in x_values:
    for N in N_values:
        cos_t = cos_approx(x, N)
        sin_t = sin_approx(x, N)
        cos_exact = np.cos(x)
        sin_exact = np.sin(x)
        print (f"Cosine values from taylor expansion and numpy calucation for x value {x} and no. of itteration {N}")
        print(cos_t)
        print(cos_exact)
        print (f"sine values from taylor expansion and numpy calucation for x value {x} and no. of itteration {N}")
        print(sin_t)
        print(sin_exact)
