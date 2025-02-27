from shape import Shape
from point import Point


class Square(Shape):
    is_side: float
    its_top_left: Point

    def draw(self) -> None:
        print("Draw square")