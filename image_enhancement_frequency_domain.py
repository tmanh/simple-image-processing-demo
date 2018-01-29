from header import *


def lowpass_filter(image, size=30):
    img_float32 = np.float32(image)
    dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = image.shape
    crow, ccol = rows/2 , cols/2     # center

    # create a mask first, center square is 1, remaining all zeros
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-size:crow+size, ccol-size:ccol+size] = 1

    # apply mask and inverse DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    return img_back


# A = 2, A = 2.7
def highpass_filter(image, A=2.0, size=30):
    img_float32 = np.float32(image)
    dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = image.shape
    crow, ccol = rows/2 , cols/2     # center

    # create a mask first, center square is 1, remaining all zeros
    highpass_mask = np.ones((rows, cols, 1), np.uint8)
    highpass_mask[crow-size:crow+size, ccol-size:ccol+size] = 0

    highboost_mask = np.ones((rows, cols, 1), np.uint8) * (A - 1)
    highboost_mask = highboost_mask + highpass_mask

    # apply mask and inverse DFT
    fshift_highpass = dft_shift*highpass_mask
    f_ishift_highpass = np.fft.ifftshift(fshift_highpass)
    img_back_highpass = cv2.idft(f_ishift_highpass)
    img_back_highpass = cv2.magnitude(img_back_highpass[:,:,0], img_back_highpass[:,:,1])

    # apply mask and inverse DFT
    fshift_highboost = dft_shift*highboost_mask
    f_ishift_highboost = np.fft.ifftshift(fshift_highboost)
    img_back_highboost = cv2.idft(f_ishift_highboost)
    img_back_highboost = cv2.magnitude(img_back_highboost[:,:,0], img_back_highboost[:,:,1])

    return img_back_highpass, img_back_highboost
