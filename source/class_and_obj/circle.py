from source.class_and_obj.geometrical_shape import GeometricShape


class Circle(GeometricShape):
    def __init__(self, name_shape, radius):
        super().__init__(name_shape)
        self.PI = 3.14
        self.r = radius

    def get_area(self):

        area = self.PI * (self.r * self.r)
        print(f"Area of '{self.name}' is {area}")
