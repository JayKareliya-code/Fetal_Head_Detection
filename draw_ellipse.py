from libs import *


def create_ellipse_array(horizontal_distance, vertical_distance, center, dimensions=(100, 100), border_width=3):
    # These are the semi-axes lengths (a and b)
    a = horizontal_distance
    b = vertical_distance

    # Center coordinates
    center_y, center_x = center

    # Creating a grid of points
    y, x = np.ogrid[:dimensions[0], :dimensions[1]]

    # Adjust coordinates relative to the center
    y = y - center_y
    x = x - center_x

    # Equation of the ellipse (x/a)^2 + (y/b)^2 = 1
    distance = (x / a)**2 + (y / b)**2

    # Define the border range
    lower_bound = 1 - border_width/a
    upper_bound = 1 + border_width/a

    # Creating an array for the ellipse border
    ellipse_border_array = np.zeros(dimensions)
    ellipse_border_array[(distance > lower_bound) & (distance < upper_bound)] = 1

    return ellipse_border_array

def display_ellipse(ellipse_array):
    plt.imshow(ellipse_array, cmap='gray')
    plt.axis('off')
    plt.show()

def overlay_ellipse_on_image(image, ellipse_array):
    # Create an RGB image with the same shape as the input grayscale image
    overlay_image = np.stack([image, image, image], axis=-1)

    # Assuming the ellipse array contains 0s and 1s
    # Here we set the ellipse pixels to red (255, 0, 0) on the image
    overlay_image[ellipse_array == 1] = [255, 0, 0]
    return overlay_image


if __name__ == '__main__':
    pass

# # Example usage
# horizontal_distance = 471  # Semi-major axis
# vertical_distance = 400   # Semi-minor axis
#
# image_array = io.imread('fatal-head.jpg',"L")
# ellipse_array = create_ellipse_array(horizontal_distance, vertical_distance,(470,538),dimensions=image_array.shape)
#
#
# merged_array = overlay_ellipse_on_image(image_array, ellipse_array)
# display_image(merged_array)
