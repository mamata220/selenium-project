from source.class_and_obj.geometrical_shape import GeometricShape


class Triangle(GeometricShape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.b = base
        self.h = height

    def get_area(self):
        area = (self.b * self.h) / 2
        print(f"Area of '{self.name}' is {area}")
