# Reto-tres

## Ejercicio de clase
**Clase línea**
```
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
```

**Clase rectángulo**
```
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

class Rectangle:
    def __init__(self, top_line, right_line, bottom_line, left_line):
        self.top_line = top_line
        self.right_line = right_line
        self.bottom_line = bottom_line
        self.left_line = left_line

    def compute_area(self):
        base = self.bottom_line.compute_lenght()
        height = self.left_line.compute_lenght()
        return base * height
    
    def compute_perimeter(self):
        base = self.bottom_line.compute_lenght()
        height = self.left_line.compute_lenght()
        return (base * 2) + (height * 2)
    
first_point = Point(0, 0)
second_point = Point(5, 0)
third_point = Point(5, 3)
fourth_point = Point(0, 3)

bottom_line = Line(first_point, second_point)
right_line = Line(second_point, third_point)
top_line = Line(third_point, fourth_point)
left_line = Line(fourth_point, first_point)

rectangle = Rectangle(top_line, right_line, bottom_line, left_line)

print("Area: ", rectangle.compute_area())
print("Perimeter: ", rectangle.compute_perimeter())
```
