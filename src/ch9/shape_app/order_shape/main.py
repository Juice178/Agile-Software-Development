from draw_all_shapes import draw_all_shapes
from circle import Circle
from square import Square
from point import Point


def main() -> None:
    c1 = Circle(is_radius=3.0, its_center=Point(x=2,y=0))
    c2 = Circle(is_radius=3.0, its_center=Point(x=2,y=0))
    c3 = Circle(is_radius=3.0, its_center=Point(x=2,y=0))
    s1 = Square(is_side=3.0, its_top_left=Point(x=2,y=0))
    s2 = Square(is_side=3.0, its_top_left=Point(x=2,y=0))
    s3 = Square(is_side=3.0, its_top_left=Point(x=2,y=0))

    all_shapes = [s1, c1, s1, c2, s3, c3]

    draw_all_shapes(all_shapes, len(all_shapes))


if __name__ == "__main__":
    main()