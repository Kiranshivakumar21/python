import math
r, h_cyl = 2, 5
surface_cylinder = 2 * math.pi * r * h_cyl + 2 * math.pi * r ** 2
volume_cylinder = math.pi * r ** 2 * h_cyl
print(surface_cylinder, volume_cylinder)
