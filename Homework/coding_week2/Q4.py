from math import sqrt
def areaTriangle (x1, y1, x2, y2, x3, y3):
    side1 = sqrt ((x1 - x2)**2 + (y1 - y2)**2)
    side2 = sqrt ((x2 - x3)**2 + (y2 - y3)**2)
    side3 = sqrt ((x3 - x1)**2 + (y3 - y1)**2)
    s = 0.5 * (side1 + side2 + side3)
    area = sqrt (s * (sqrt((s - side1)**2) * (sqrt((s - side2)**2) * (sqrt((s - side3)**2)))))
    return area
    
# Use abs() for absolute values

# Use ** 0.5 for sqrt