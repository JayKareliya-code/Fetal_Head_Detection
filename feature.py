import matplotlib.pyplot as plt

from libs import np

kernelEdge = {
    'a': np.array([[1, -1],
                   [1, -1]]),

    'b': np.array([[1, 1],
                   [-1, -1]]),

    'c': np.array([[1, 1, -1],
                   [-1, -2, -1],
                   [-1, 1, 1]]),

    'd': np.array([[-1, -1, 1],
                   [1, -2, 1],
                   [1, -1, -1]])
}
kernelLine = {

    'a': np.array([[1, 1, 1],
                   [0, 0, 0],
                   [1, 1, 1]]),

    'b': np.array([[1, 0, 1],
                   [1, 0, 1],
                   [1, 0, 1]]),

    'c': np.array([[1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 0, 0, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 0, 0, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1]]),

    'd': np.array([[1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 1, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1]])
}
kernelCentreSurround = {

    'a': np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]]),

    'b': np.array([[1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1]]),
}
kernelRectangle = {

    'a': np.array([[1, 0],
                   [0, 1]]),

    'b': np.array([[1, 1, 1, 1],
                   [0, 0, 0, 0],
                   [1, 1, 1, 1]])
}

sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

mean_kernel = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]], dtype=np.float32) / 9
fig, axs = plt.subplots(4, max(len(kernelEdge), len(kernelLine), len(kernelCentreSurround), len(kernelRectangle)), figsize=(12, 10))

# Set titles for each row
axs[0, 0].set_title('Feature Edge')
axs[1, 0].set_title('Feature Line')
axs[2, 0].set_title('Feature Centre Surround')
axs[3, 0].set_title('Feature Rectangle')

# Helper function to plot kernels
def plot_kernels(row, kernel_dict):
    for i, (key, kernel) in enumerate(kernel_dict.items()):
        axs[row, i].imshow(kernel, cmap='gray')
        axs[row, i].set_title(f'Kernel {key}')
        axs[row, i].axis('off')

# Plot each category of kernels
plot_kernels(0, kernelEdge)
plot_kernels(1, kernelLine)
plot_kernels(2, kernelCentreSurround)
plot_kernels(3, kernelRectangle)

# Adjust layout and display the plot

plt.show()
