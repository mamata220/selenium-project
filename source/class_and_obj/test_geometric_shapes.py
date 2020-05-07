from source.class_and_obj.geometrical_shape import GeometricShape
from source.class_and_obj.circle import Circle
from source.class_and_obj.square import Square
from source.class_and_obj.triangle import Triangle


circle1 = Circle('circle', 5)
circle1.get_area()

square1 = Square('square', 5, 3)
square1.get_area()

triangle1 = Triangle("triangle", 4, 4)
triangle1.get_area()
