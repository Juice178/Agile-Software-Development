from draw_all_shapes import draw_all_shapes
from shape import ShapeType
from circle import Circle
from square import Square
from point import Point


def main() -> None:
    c = Circle(its_type=ShapeType.CIRCLE, is_radius=3.0, its_center=Point(x=2,y=0))
    s = Square(its_type=ShapeType.SQUARE, is_side=3.0, its_top_left=Point(x=2,y=0))

    all_shapes = [c, s]

    draw_all_shapes(all_shapes, len(all_shapes))


if __name__ == "__main__":
    main()