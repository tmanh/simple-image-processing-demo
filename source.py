from demo_io import *
from image_enhancement_spatial_domain import *
from image_enhancement_frequency_domain import *


def demo_negative_image():
    origin = get_image('gray')
    cv2.imshow('Origin', origin)
    cv2.imshow('Negative', negative_image(origin))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo_power_law_transformation():
    origin = get_image('gray')
    gamma = get_real_number('Enter gamma (real number): ')

    cv2.imshow('Origin', origin)
    cv2.imshow('Power Law', power_law(origin, gamma=gamma))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_histogram():
    origin = get_image('gray')
    histogram = cv2.calcHist([origin], [0], None, [256], [0, 256])

    plt.subplot(121), plt.imshow(origin, 'gray')
    plt.subplot(122), plt.plot(histogram)
    plt.xlim([0, 256])
    plt.show()


def demo_histogram_equalization():
    origin = get_image('gray')
    equalizedImage = cv2.equalizeHist(origin)

    cv2.imshow('Origin', origin)
    cv2.imshow('Equalization', equalizedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo_otsu_binarization():
    origin = get_image('gray')
    ret1,th1 = cv2.threshold(origin, 127, 255, cv2.THRESH_BINARY)
    ret2,th2 = cv2.threshold(origin, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(origin, (5,5), 0)
    ret3,th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
              'Original Noisy Image','Histogram',"Otsu's Thresholding",
              'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

    images = [origin, 0, th1, origin, 0, th2, blur, 0, th3]


    for i in xrange(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_mean_filter():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    smooth_image = mean_filter(origin, kernel_size)

    cv2.imshow('Origin', origin)
    cv2.imshow('Smooth', smooth_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo_gaussian_filter():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    smooth_image = gaussian_filter(origin, kernel_size)

    cv2.imshow('Origin', origin)
    cv2.imshow('Smooth', smooth_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo_median_filter():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    smooth_image = cv2.medianBlur(origin, kernel_size)

    cv2.imshow('Origin', origin)
    cv2.imshow('Smooth', smooth_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo_laplacian_filter():
    origin = get_image('gray')
    laplacian_image, sharpened_image = laplacian_sharpening(origin)

    plt.subplot(1,3,1),plt.imshow(origin,'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,2),plt.imshow(laplacian_image,'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,3),plt.imshow(sharpened_image,'gray')
    plt.title('Sharpened'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_lowpass_filter():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    smooth_image = lowpass_filter(origin, size=kernel_size)

    plt.subplot(121),plt.imshow(origin, cmap = 'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(smooth_image, cmap = 'gray')
    plt.title('Smooth'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_highpass_filter():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number, small number): ')
    A = get_real_number('Enter kernel size (real number, A >= 1, special A: 2, 2.7): ')
    highpass_image, sharpened_image = highpass_filter(origin, A=A, size=kernel_size)

    plt.subplot(131),plt.imshow(origin, cmap = 'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(highpass_image, cmap = 'gray')
    plt.title('Highpass'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(sharpened_image,'gray')
    plt.title('Sharpened'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_erosion():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    iterations = get_integer_number('Enter number of iterations (integer number): ')

    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    erosion = cv2.erode(origin, kernel, iterations = iterations)

    plt.subplot(121),plt.imshow(origin, cmap = 'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(erosion, cmap = 'gray')
    plt.title('Erosion'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_dilation():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    iterations = get_integer_number('Enter number of iterations (integer number): ')

    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    dilation = cv2.dilate(origin, kernel, iterations = iterations)

    plt.subplot(121),plt.imshow(origin, cmap = 'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dilation, cmap = 'gray')
    plt.title('Dilation'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_opening():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    iterations = get_integer_number('Enter number of iterations (integer number): ')

    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    opening = cv2.morphologyEx(origin, cv2.MORPH_OPEN, kernel, iterations = iterations)

    plt.subplot(121),plt.imshow(origin, cmap = 'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(opening, cmap = 'gray')
    plt.title('Opening'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo_closing():
    origin = get_image('gray')
    kernel_size = get_integer_number('Enter kernel size (integer number): ')
    iterations = get_integer_number('Enter number of iterations (integer number): ')

    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    closing = cv2.morphologyEx(origin, cv2.MORPH_CLOSE, kernel, iterations = iterations)

    plt.subplot(121),plt.imshow(origin, cmap = 'gray')
    plt.title('Origin'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(closing, cmap = 'gray')
    plt.title('Closing'), plt.xticks([]), plt.yticks([])
    plt.show()


def choose_basic_gray_level_transformation():
    _end_choose_basic_gray_level_transformation = False

    while(not _end_choose_basic_gray_level_transformation):
        max_choice = print_choose_basic_gray_level_transformation()
        mode = get_input(max_choice=max_choice)

        if mode == 0:
            _end_choose_basic_gray_level_transformation = True
        elif mode == 1:
            demo_negative_image()
        elif mode == 2:
            demo_power_law_transformation()


def choose_smoothing_and_sharpening_spatial():
    _end_choose_smoothing_and_sharpening_spatial = False

    while(not _end_choose_smoothing_and_sharpening_spatial):
        max_choice = print_choose_smoothing_and_sharpening_spatial()
        mode = get_input(max_choice=max_choice)

        if mode == 0:
            _end_choose_smoothing_and_sharpening_spatial = True
        elif mode == 1:
            demo_mean_filter()
        elif mode == 2:
            demo_gaussian_filter()
        elif mode == 3:
            demo_median_filter()
        elif mode == 4:
            demo_laplacian_filter()


def choose_smoothing_and_sharpening_frequency():
    _end_choose_smoothing_and_sharpening_frequency = False

    while(not _end_choose_smoothing_and_sharpening_frequency):
        max_choice = print_choose_smoothing_and_sharpening_frequency()
        mode = get_input(max_choice=max_choice)

        if mode == 0:
            _end_choose_smoothing_and_sharpening_frequency = True
        elif mode == 1:
            demo_lowpass_filter()
        elif mode == 2:
            demo_highpass_filter()


def choose_histogram_processing():
    _end_choose_histogram_processing = False

    while(not _end_choose_histogram_processing):
        max_choice = print_choose_histogram_processing()
        mode = get_input(max_choice=max_choice)

        if mode == 0:
            _end_choose_histogram_processing = True
        elif mode == 1:
            show_histogram()
        elif mode == 2:
            demo_histogram_equalization()
        elif mode == 3:
            demo_otsu_binarization()


def choose_morphological_processing():
    _end_choose_morphological_processing = False

    while(not _end_choose_morphological_processing):
        max_choice = print_choose_morphological_processing()
        mode = get_input(max_choice=max_choice)

        if mode == 0:
            _end_choose_morphological_processing = True
        elif mode == 1:
            demo_dilation()
        elif mode == 2:
            demo_erosion()
        elif mode == 3:
            demo_opening()
        elif mode == 4:
            demo_closing()


def choose_task():
    _end_demo = False

    while(not _end_demo):
        max_choice = print_choose_task_description()
        mode = get_input(max_choice=max_choice)

        if mode == 0:
            _end_demo = True
        elif mode == 1:
            choose_basic_gray_level_transformation()
        elif mode == 2:
            choose_smoothing_and_sharpening_spatial()
        elif mode == 3:
            choose_smoothing_and_sharpening_frequency()
        elif mode == 4:
            choose_histogram_processing()
        elif mode == 5:
            choose_morphological_processing()


if __name__ == '__main__':
    choose_task()
