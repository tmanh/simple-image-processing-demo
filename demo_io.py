from header import *


def print_choose_basic_gray_level_transformation():
    print '\n'
    print 'Choose image processing technique:'
    print '1. Image Negatives'
    print '2. Power-Law Transformations'
    print '0. Back'
    return 2


def print_choose_smoothing_and_sharpening_spatial():
    print '\n'
    print 'Choose image processing technique:'
    print '1. Mean Filters (Smoothing)'
    print '2. Gaussian Filters (Smoothing)'
    print '3. Median Filters (Smoothing)'
    print '4. Laplacian Filters (Sharpening)'
    print '0. Back'
    return 4


def print_choose_smoothing_and_sharpening_frequency():
    print '\n'
    print 'Choose image processing technique:'
    print '1. Ideal Lowpass Filters (Smoothing)'
    print '2. Ideal Highpass Filters (Sharpening)'
    print '0. Back'
    return 2


def print_choose_histogram_processing():
    print '\n'
    print 'Choose image processing technique:'
    print '1. Compute Histogram'
    print '2. Histogram Equalization'
    print '3. Otsu\'s Binarization'
    print '0. Back'
    return 3


def print_choose_morphological_processing():
    print '\n'
    print 'Choose image processing technique:'
    print '1. Dilation'
    print '2. Erosion'
    print '3. Opening'
    print '4. Closing'
    print '0. Back'
    return 4


def print_choose_task_description():
    print '\n'
    print 'Choose image processing technique:'
    print '1. Basic Gray Level Transformations'
    print '2. Smoothing and Sharpening (Spatial Domain)'
    print '3. Smoothing and Sharpening (Frequency Domain)'
    print '4. Histogram Processing'
    print '5. Morphological Image Processing'
    print '0. Exit'
    return 5


def get_input(max_choice):
    mode = -1
    while(mode == -1 or mode > max_choice):
        try:
            mode = int(raw_input('Enter your choice: '))

            if mode > max_choice or mode < 0:
                print "Please enter a number from 0 to {0}.".format(max_choice)

            return mode
        except ValueError:
            print "Please enter a number."


def get_real_number(message):
    received_valid_real_number = False

    while(not received_valid_real_number):
        try:
            number = float(raw_input(message))
            return number
        except ValueError:
            print "Please enter a number."


def get_integer_number(message):
    received_valid_integer_number = False

    while(not received_valid_integer_number):
        try:
            number = int(raw_input(message))
            return number
        except ValueError:
            print "Please enter a number."


def get_image_path():
    print '\n'
    path = raw_input("Enter your image: ")
    return path


def get_image(mode='gray'):
    if mode == 'gray':
        image = cv2.imread(get_image_path(), 0)
    elif mode == 'color':
        image = cv2.imread(get_image_path())

    return image
