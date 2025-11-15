import numpy as np
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
mymodel = np.poly1d(np.polyfit(x, y, 2))
z = float(input(''))
output_value = mymodel(z)
print(output_value)