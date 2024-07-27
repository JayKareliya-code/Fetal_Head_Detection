import matplotlib.pyplot as plt
import numpy as np
from skimage import io,morphology,filters
from skimage.util import img_as_ubyte
from sklearn.cluster import KMeans
from skimage.morphology import skeletonize
import convolution as cv
import feature as ft
import cv2
from PIL import Image
import math
import os

