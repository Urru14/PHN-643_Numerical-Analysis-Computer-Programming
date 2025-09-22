import numpy as np
dx = 100 #meter
dy = np.array([300,380,340,230,240,320,375,345,110])
print ("The surface area of a lake is estimated by measuring the width of the lake at intervals of 100 m are: \n300,380,340,230,240,320,375,345,110 ")
print ("By numerical integration estimated the area of the lake = interval * sum of surface area:")
print ("100*(300+380+340+230+240+320+375+345+110)")
y = np.sum(dy)
area = dx*y
print (f"Therefore area equals to {area} meters")
