def get_distance_metrics(arr):
    distance = []
    # Loop over each point in the given array
    for point in range(len(arr)):
        # Find all similar points, extract to the separate inner array and return initial indices of the points
        point_metrics = [i for i, x in enumerate(arr) if x == arr[point]]
        result = [abs(point_metrics[point_metrics.index(point)] - el) for el in point_metrics]
        distance.append(sum(result))
    return distance
#[0, 3, 5] #[1, 2] #[1, 2] #[0, 3, 5] #[4] #[0, 3, 5]
#[8, 1, 1, 5, 0, 7]
print(get_distance_metrics([1, 2, 2, 1, 5, 1]))
