import matplotlib.pyplot as plt

from libs import *


class Preprocess:
    """
    This is Parent Class of ImageBinary Class
    -> Takes the image path and show the image
    """
    def __init__(self):
        pass

    @staticmethod
    def show_img(image: classmethod,title=None) -> None:
        plt.imshow(image,cmap='binary')
        plt.title(title)
        plt.show()

    @staticmethod
    def read_image(path: str, gray=True) -> classmethod:
        if path is not None:
            gray_image = io.imread(path, 'L')
            return gray_image
        else:
            return print("Image Path is not Valid")


class ImageBinary(Preprocess):
    """
    This is the children class and extends from the Preprocess class
    To Use this class we first call the Preprocess and then use this class
    """

    def __init__(self):
        Preprocess.__init__(self)

    @staticmethod
    def get_final_image(image: classmethod, skeleton=False, threshold=False) -> classmethod:
        """
        :param image: An Image array you want to use
        :param skeleton: False by default
        :param threshold: False by default
        :return: Final Image when this class is called
        """
        featured_image = ImageBinary.extract_feature(image)
        if threshold:
            threshold_image = ImageBinary.threshold(featured_image)
            final_image = ImageBinary.filter(threshold_image,skeleton=skeleton)
        else:
            final_image = ImageBinary.filter(featured_image, skeleton=skeleton)
        return final_image

    @staticmethod
    def extract_feature(image: classmethod) -> classmethod:
        """Extract the feature EDGE and CentreSurround"""

        # Feature EDGE
        sum1 = np.sum(ft.kernelEdge['d'])
        for i in range(2):
            image = cv.convolve2D(image, ft.kernelEdge['d'] / sum1, 1)

        # Feature CentreSurround
        sum2 = np.sum(ft.kernelCentreSurround['b'])
        for i in range(3):
            image = cv.convolve2D(image, ft.kernelCentreSurround['b'] / sum2, 2)

        Preprocess.show_img(image,title="Processed Image")
        return image

    @staticmethod
    def threshold(image: classmethod) -> classmethod:
        """ Thresholding to remove the not focused part from the image
         mostly used to create a binary image """

        img = cv2.convertScaleAbs(image)
        thresh = filters.threshold_otsu(img)
        binary = img > thresh
        Preprocess.show_img(binary,title="After thresholding and feature Extraction")
        return binary

    @staticmethod
    def filter(image: classmethod, skeleton=False) -> classmethod:
        """
        :param image:
        :param skeleton: True if you want only skeleton of the image
        :return: image
        """

        filter_array = morphology.disk(10)
        for i in range(2):
            image = morphology.opening(image, filter_array)
            image = morphology.closing(image, filter_array)
        if skeleton:
            image = skeletonize(image)
            image = morphology.closing(image, filter_array)
            Preprocess.show_img(image, title="Skeleton Image")
            return image
        else:
            Preprocess.show_img(image, title="Filtered Binary Image")
            return image

if __name__ == '__main__':
    pass