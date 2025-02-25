from shape import ShapeType
from point import Point
from pydantic import BaseModel

class Circle(BaseModel):
    its_type: ShapeType
    is_radius: float
    its_center: Point


def draw_circle(circle: Circle):
    print("Draw circle")