# 
class Shape:
    def __init__(self,radius,color) -> None:
        self.radius = radius
        self.color= color
    
    def draw(self):
        print(f"drawing a shape with radius {self.radius}, color: {self.color}")

class Circle(Shape):
    def __init__(self, radius, color,center) -> None:
        super().__init__(radius, color)
        self.center = center
    
    def draw(self):
        super().draw()
        print(f"center of the circle {self.center}")


circle = Circle(5,"red", (0,0))
circle.draw()