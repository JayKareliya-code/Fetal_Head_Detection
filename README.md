
# Fetal Head Detection Using Image Processing

This project aims to detect the fetal head using image processing techniques in Python, leveraging the powerful libraries sklearn and skimage. The process involves several steps including noise reduction, edge detection, threshold filtering, skeletonization, center detection, and ellipse fitting to approximate the circumference of the fetal head.

## Project Structure

```
Fetal_Head_Detection/
├── test_results/
├── convolution.py
├── draw_ellipse.py
├── feature.py
├── find_center.py
├── libs.py
├── main.py
├── Process.py
├── requirements.txt
└── test-image.jpg
```

## Description of Files

- **test_results/**: Example results are stored for the reference.
- **convolution.py**: Contains functions for applying convolution operations.
- **draw_ellipse.py**: Includes functions for drawing ellipses on the images.
- **feature.py**: Responsible for extracting features from the images.
- **find_center.py**: Implements the K-Means algorithm to find the center of the fetal head.
- **libs.py**: Contains utility functions and libraries used across the project.
- **main.py**: The main script to run the entire fetal head detection process.
- **Process.py**: Implements the overall image processing pipeline.
- **requirements.txt**: Lists the dependencies required to run the project.
- **test-image.jpg**: A sample image used for testing the implementation.

## Installation

1. Clone the repository:
   ```sh
   git clone <[repository_link](https://github.com/JayKareliya-code/Fetal_Head_Detection.git)>
   ```
2. Navigate to the project directory:
   ```sh
   cd Fetal_Head_Detection
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main script to start the fetal head detection process:
```sh
python main.py
```

The `main.py` script will process the `test-image.jpg`.

## Steps Involved in Detection

1. **Grayscale Image Acquisition**: Convert the fetal head images into grayscale.
2. **Noise Reduction**: Apply a Gaussian filter to remove noise.
3. **Edge Detection**: Detect edges using kernels and convert the image to a binary format.
4. **Threshold Filtering**: Extract a rough boundary of the fetal head by filtering the image using a threshold.
5. **Skeletonization**: Obtain the mean values of the boundary representing the circumference of the fetal head.
6. **Center Detection**: Use the K-Means algorithm to find the center of the fetal head.
7. **Ellipse Fitting**: Determine the major and minor axes and fit an ellipse to the detected boundary.
8. **Overlay and Measurement**: Overlay the fitted ellipse onto the original image to approximate the circumference of the fetal head.


## Contact

For any questions or feedback, please contact me via [LinkedIn](www.linkedin.com/in/jay-kareliya).
if not works you can copy the URL: www.linkedin.com/in/jay-kareliya

---

By following these instructions, you should be able to replicate the process of detecting the fetal head using image processing techniques.
