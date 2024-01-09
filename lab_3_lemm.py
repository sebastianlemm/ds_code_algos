def cPairDist(points):
    # sort the list of points
    sorted_points = sorted(points)
    # pass sorted list to the recursive function
    return recCPairDist(sorted_points)

def recCPairDist(points):
    # Base case: If there are 2 or fewer points, return the absolute difference between them.
    if len(points) <= 2:
        return abs(points[1] - points[0]) if len(points) == 2 else float('inf')
    
    # Divide the list in two
    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    # Conquer: Find the closest pair distance in each sublist
    left_dist = recCPairDist(left_half)
    right_dist = recCPairDist(right_half)
    
    # Combine: compute the remaining distance
    cross_dist = abs(left_half[-1] - right_half[0])
    
    # Return the minimum of the three distances
    return min(left_dist, right_dist, cross_dist)

# Test cases
test_cases = [[7, 4, 12, 14, 2, 10, 16, 6],
              [7, 4, 12, 14, 2, 10, 16, 5],
              [14, 8, 2, 6, 3, 10, 12]]

for points in test_cases:
    print(f"List of points: {points}")
    print(f"Closest pair distance: {cPairDist(points)}")
    print("------")



### output ###
# List of points: [7, 4, 12, 14, 2, 10, 16, 6]
# Closest pair distance: 1
# ------
# List of points: [7, 4, 12, 14, 2, 10, 16, 5]
# Closest pair distance: 1
# ------
# List of points: [14, 8, 2, 6, 3, 10, 12]
# Closest pair distance: 1
# ------