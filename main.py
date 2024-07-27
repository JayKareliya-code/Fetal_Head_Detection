from libs import *
from Process import Preprocess, ImageBinary
from find_center import get_centre
from draw_ellipse import create_ellipse_array,overlay_ellipse_on_image


"""
UseCase: Fetal Head Detection using the image processing
Author : Jay Kareliya
About : Graduate Student at Concordia University
Team members : 1) Jay Kareliya - (40195706)
               2) Kathan Prajapati - (40255893)
               3) Twinkal Christian - (40255894)              
"""


class Runner:
    """
    Main Class to execute the all the steps
    """
    def __init__(self, path: str) -> None:
        self.path = path

        # get the original image, preprocess it and show it
        original_image = Preprocess().read_image(self.path, gray=True)
        Preprocess().show_img(original_image,"Original Image Gray Scale")

        # feature extract and convert it to skeleton
        skeleton_image = ImageBinary.get_final_image(image=original_image, skeleton=True, threshold=True)

        # find the center of the ellipse and try to fit in the image provided
        cx,cy,mV,mH = get_centre(skeleton_image)
        print(f"Centre X, {cx} \n Centre Y, {cy} \n Maximum vertical Distance , {mV} \n Maximum Horizontal Distance, {mH}")
        ellipse_array = create_ellipse_array(mH,mV,(cx,cy),original_image.shape)
        final_image = overlay_ellipse_on_image(original_image,ellipse_array)
        Preprocess.show_img(final_image,"Final Output")


if __name__ == '__main__':
    run = Runner('test-image.jpg')  # add path to the image
