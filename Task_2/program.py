import math

def read_circle_data(file_path):
    with open(file_path, 'r') as f:
        center_x, center_y = [float(i) for i in f.readline().strip().split()]
        radius = float(f.readline().strip())
    return (center_x, center_y, radius)

def read_points(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y = [float(i) for i in line.strip().split()]
            points.append((x, y))
    return points

def point_position(center_x, center_y, radius, point):
    point_x, point_y = point
    distance_squared = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

    if distance_squared < radius:
        return 1  # точка внутри
    elif distance_squared == radius:
        return 0  # точка на окружности
    else:
        return 2  # точка снаружи

def main(circle_file, points_file):
    center_x, center_y, radius = read_circle_data(circle_file)
    
    points = read_points(points_file)

    for point in points:
        position = point_position(center_x, center_y, radius, point)
        print(position)

if __name__ == "__main__":
    circle_file, points_file = input().split()
    main(circle_file, points_file)