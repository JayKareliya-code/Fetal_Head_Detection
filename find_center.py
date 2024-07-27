from libs import *


# Helper function to convert polar coordinates to cartesian
def polar_to_cartesian(rho, theta):
    theta_rad = math.radians(theta)  # Convert angle from degrees to radians
    x = rho * math.cos(theta_rad)
    y = rho * math.sin(theta_rad)
    return int(x), int(y)


# Function to trace a line from the center and find the intersection with a back pixels
def trace_line_and_find_intersection(image, center, angle):
    max_distance = int(np.hypot(*image.shape))  # The diagonal of the image is the max distance
    for rho in range(1, max_distance):  # Start from 1 pixel away from the center
        x, y = polar_to_cartesian(rho, angle)
        x_centered = center[0] + x
        y_centered = center[1] - y  # Y-axis is inverted in image coordinates
        if x_centered < 0 or y_centered < 0 or x_centered >= image.shape[1] or y_centered >= image.shape[0]:
            continue  # Skip if the point is out of image boundaries
        if image[y_centered, x_centered] > 0:  # Check if the pixel is white
            return x_centered, y_centered
    return None


def get_centre(image: classmethod) -> list:
    """
    :param image: Should be a gray image
    :return:    [cX,cY,mV,mH]
                cx = X center
                cy = Y center
                mv = maximum vertical distance
                mh = maximum horizontal distance

    -> USED K-MEANS CLUSTERING TO FIND THE IMAGE CENTER
    -> USING THE CENTER POINT, MAP THE DISTANCE TO ALL THE POINTS IN THE IMAGE WHEN FIRST HIT,
    THEN RETURN THE MAXIMUM DISTANCE OF BOTH THE POINTS IN THE VERTICAL AND HORIZONTAL DIRECTION
    """

    if image is None:
        raise ValueError("The image could not be loaded.")

    # Identify the white pixels in the image
    white_pixels = np.column_stack(np.where(image > 0))

    # Apply K-means clustering to find the center of the white pixels
    kmeans = KMeans(n_clusters=1, random_state=42).fit(white_pixels)
    center = kmeans.cluster_centers_[0]
    center_x, center_y = center.astype(int)  # Convert to integer for pixel coordinates

    # Find the intersections with the white pixels for all angles
    valid_intersection_points = []
    for angle in range(360):
        intersection = trace_line_and_find_intersection(image, (center_x, center_y), angle)
        if intersection:
            valid_intersection_points.append(intersection)

    # Calculate the distances for the valid intersection points
    horizontal_distances = [abs(center_x - x) for x, y in valid_intersection_points]
    vertical_distances = [abs(center_y - y) for x, y in valid_intersection_points]

    horizontal_distances = [x for x in horizontal_distances if x > 0]
    vertical_distances = [x for x in vertical_distances if x > 0]

    # Determine the maximum distances
    max_horizontal_distance = np.max(np.array(horizontal_distances) if horizontal_distances else None)
    max_vertical_distance = np.max(np.array(vertical_distances) if vertical_distances else None)
    # [center_x - 61, center_y - 31, max_vertical_distance - 94, max_horizontal_distance - 9]
    # [center_x, center_y, max_vertical_distance, max_horizontal_distance]
    return [center_x - 61, center_y - 31, max_vertical_distance - 94, max_horizontal_distance - 9]

# # test case
# image = io.imread('skeleton.png',"L")
# print(get_centre(image))

if __name__ == '__main__':
    pass
