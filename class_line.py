class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def compute_lenght(self):
        lenght = ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**(0.5)
        return lenght
    
    def compute_slope(self):
        slope = (self.end.y - self.start.y)/(self.end.x - self.start.x)
        return slope
    
    def compute_horizontal_cross(self):
        if self.start.y <= 0 and self.end.y >= 0:
            return "True"
        elif self.start.y >= 0 and self.end.y <=0:
            return "True"
        elif self.start.y >= 0 and self.end.y >= 0:
            return "False"
        elif self.start.y <= 0 and self.end.y <=0:
            return "False"
        else:
            return ""
    
    def compute_vertical_cross(self):
        if self.start.x <= 0 and self.end.x >= 0:
            return "True"
        elif self.start.x >= 0 and self.end.x <= 0:
            return "True"
        elif self.start.x >= 0 and self.end.x >= 0:
            return "False"
        elif self.start.x <= 0 and self.end.x <=0:
            return "False"
        else:
            return ""

first_point = Point(1, 1)
second_point = Point(3, -2)
line = Line(first_point, second_point)
print("Lenght: ", line.compute_lenght())
print("Slope: ", line.compute_slope())
print("Horizontal cross: ", line.compute_horizontal_cross())
print("Vertical cross: ", line.compute_vertical_cross())