from shape import Shape

def draw_all_shapes(shape_pointer: list[Shape], n: int) -> None:
    for i in range(n):
        s: Shape = shape_pointer[i]
        s.draw()
