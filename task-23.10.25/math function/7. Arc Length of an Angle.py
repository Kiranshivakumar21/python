def arc_length(radius, angle_degree):
    import math
    return 2 * math.pi * radius * (angle_degree / 360)
print(arc_length(5, 60))
