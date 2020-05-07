from source.class_and_obj.geometrical_shape import GeometricShape


class Square(GeometricShape):

    def __init__(self, name, width, height):
        super().__init__(name)
        self.w = width
        self.h = height

    def get_area(self):
        area = self.w * self.h
        print(f"Area of '{self.name}' is {area}")