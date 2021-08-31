from polygon import Polygon
from shape import Shape
class Triangle(Polygon,Shape):
    def area(self):
        return  0.5 * self.get_height()* self.get_width()
