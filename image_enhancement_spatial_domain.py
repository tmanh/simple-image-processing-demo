from header import *


def negative_image(image):
    negative = 255 - image
    return negative


# Power law transformation
def power_law(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


def mean_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))


def gaussian_filter(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def laplacian_sharpening(image):
    laplacian_kernel = np.ones((3,3)) * (-1)
    laplacian_kernel[1,1] = 8

    sharpening_kernel = np.ones((3,3)) * (-1)
    sharpening_kernel[1,1] = 9

    # I am using two kernel instead of applying Laplacian kernel then adding
    # the result of laplacian to the image. It helps us avoid the error of
    # rounding
    laplacian = cv2.filter2D(image, -1, laplacian_kernel)
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    return laplacian, sharpened_image
