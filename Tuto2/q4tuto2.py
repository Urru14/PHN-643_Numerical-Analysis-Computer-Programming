import matplotlib.pyplot as plt
def time_to_fall(height):
    g=9.81
    dt=0.10
    time = 0
    current_height = 0.0
    
    while True :
        time += dt
        current_height = 0.5 * g * time ** 2
        if current_height > height:
            break
        print (f"{current_height:<18.2f} {time:<17.2}")
        plt.plot(current_height, time, 'ro')
            
    return time

height = float(input("Enter the height of from where object is fall freely in meters: "))

print(f"{'Height remained':<17} {'time to fall':<17}")
fall_time = time_to_fall(height)

print(f"Time to fall from {height} meters: {fall_time:.2f} seconds")
plt.show()
