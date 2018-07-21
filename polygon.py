from math import sqrt

class Polygon:
    def __init__(self,points):
        self.points = [] #format of points: [[x,y],[x1,y1],[x2,y2]...]

    def addPoint(self,x,y):
        point = [x,y]
        self.points.append(point)
        return self.points

    def perimeter(self):
        total = 0
        count = 0
        if len(self.points) < 3:
            print("Not enough points to calculate perimeter.")
        else:
            for number in range(len(self.points)):
                count += 1
                if count >= len(self.points):
                    first = self.points[len(self.points) - 1]
                    second = self.points[0]
                else:
                     first = self.points[count]
                     second = self.points[count - 1]
                distance = sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2)
                total = total + distance
            return total

    def area(self):
        count = 0
        total = 0
        length = len(self.points)
        for number in range(length):
            count += 1
            if count >= length:
                second = self.points[length - 1]
                first = self.points[0]
            else:
                first = self.points[count]
                second = self.points[count - 1]
            area = ((first[0]*second[1]) - (second[0]*first[1]))
            total = total + area
        total = (total/2)
        return abs(total)


poly = Polygon([])
print("Enter your points as they would be connected in a graph, either clockwise or counterclockwise.")
vertices = int(input("How many vertices will be in your polygon? "))
count = 1
while count <= vertices:
    x = float(input("What x-value? "))
    y = float(input("What y-value? "))
    poly.addPoint(x,y)
    count += 1
print(poly.perimeter())
print(poly.area())
