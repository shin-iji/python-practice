import math

numOfShape = int(input("Number of Shape: "))
lengthOfShape = int(input("Length of Shape: "))
area = (numOfShape * (math.pow(lengthOfShape, 2))) / (4 * math.tan(3.14/numOfShape))
print("Polygon", numOfShape, "Shape, Length", lengthOfShape, "have area", format(area, ".3f"))