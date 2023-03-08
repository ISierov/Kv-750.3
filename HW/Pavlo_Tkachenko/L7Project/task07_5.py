# Find The Distance Between Two Points
import math
def distance2points(x1,y1, x2,y2):
    return round(math.sqrt((y1-y2)**2+(x2-x1)**2), 1)

print(distance2points(2,2,3,3))

