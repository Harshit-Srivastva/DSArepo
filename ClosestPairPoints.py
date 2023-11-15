import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def brute_force_closest_pair(points):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair

def closest_pair_recursive(points):
    n = len(points)

    if n <= 3:
        return brute_force_closest_pair(points)

    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]

    left_distance, left_pair = closest_pair_recursive(left_half)
    right_distance, right_pair = closest_pair_recursive(right_half)

    min_distance, min_pair = min((left_distance, left_pair), (right_distance, right_pair), key=lambda x: x[0])

    strip = [point for point in points if abs(point[0] - points[mid][0]) < min_distance]
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            distance = euclidean_distance(strip[i], strip[j])
            if distance < min_distance:
                min_distance = distance
                min_pair = (strip[i], strip[j])

    return min_distance, min_pair

def closest_pair(points):
    sorted_points = sorted(points, key=lambda x: x[0])
    return closest_pair_recursive(sorted_points)

# Example usage:
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_distance, closest_pair = closest_pair(points)
print("Closest Pair Distance:", min_distance)
print("Closest Pair:", closest_pair)
