from point import Point
from shape import Shape

class Circle(Shape):
    is_radius: float
    its_center: Point

    def draw(self) -> None:
        print("Draw circle")