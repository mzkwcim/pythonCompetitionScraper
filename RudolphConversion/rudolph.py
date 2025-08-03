import math


def convert_points_to_time(points, world_record):
    return world_record / math.pow((points / 1000), (1/3))



wr = 46.86
points = 559

time = convert_points_to_time(points, wr)
print(f"Converted Time: {time:.2f}")
