from triangle import Triangle
from square import Square
s1 = Square()
s1.set_value(2,3)
s1.set_color("Green")
print(s1.area(),s1.get_color())
s2 = Triangle()
s2.set_value(5,6)
s2.set_color("Blue")
print(s2.area(),s2.get_color())
