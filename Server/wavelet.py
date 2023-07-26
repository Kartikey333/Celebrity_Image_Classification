import numpy as np
import pywt
import cv2


def w2d(img, mode="haar", level=1):
    imArray = img

    # conver to gray scale
    if img is not None:

        imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)

    # convert to float
    imArray = np.float32(imArray)
    imArray /= 255;

    coeff = pywt.wavedec2(imArray, mode, level=level)

    coeff_H = list(coeff)
    coeff_H[0] *= 0;

    imArray_H = pywt.waverec2(coeff_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    return imArray_H