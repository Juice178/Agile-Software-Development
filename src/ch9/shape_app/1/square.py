from shape import ShapeType
from point import Point
from pydantic import BaseModel


class Square(BaseModel):
    its_type: ShapeType
    is_side: float
    its_top_left: Point


def draw_square(square: Square):
    print("Draw square")