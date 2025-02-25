from shape import ShapeType
from square import draw_square
from circle import draw_circle


def draw_all_shapes(shape_pointer: list, n: int) -> None:
    for i in range(n):
        s = shape_pointer[i]
        if s.its_type == ShapeType.SQUARE:
            draw_square(s)
        elif s.its_type == ShapeType.CIRCLE:
            draw_circle(s)
        else:
            pass

