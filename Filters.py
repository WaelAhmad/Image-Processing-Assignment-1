#-------------------------------------------------------------------------------
# Name:       Image Processing Filters
# Purpose:
#
# Author:      Wa'el Ahmad
#
# Created:     21/02/2018
# Copyright:   (c) Wa'el Ahmad 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2
import numpy as np
import math

# Original Image

# Read Image 
img1 = cv2.imread('salah.png', 1)

# show Image
cv2.imshow('salah_Original',img1)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_original.jpg', img1)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Average Filter

# Read Image as gray scale
img1 = cv2.imread('salah.png', 0)
mean_image = img1.copy()

# Get the dimensions of the image
width_img = img1.shape[1]
height_img = img1.shape[0]

# Iterate of sub region of the image as i need to exclude the borders
for i in np.arange(3, height_img - 3):
    for j in np.arange(3, width_img - 3):
        v = 0
        # For each pixel i need to have 3 pixels its right, 3 pixels its left, 3 pixels above it, and 3 pixels below it
        for a in np.arange(-3, 4):
            for b in np.arange(-3, 4):
                # Get all the neighbors of the pixel at position(i,j)
                # It will iterate over the neighborhood of the pixel(i,j)
                c = img1.item(i + a, j + b)
                v = v + c
        # 7*7 = 49 of the neighborhood pixels
        # Divide with 49 to get the average
        d = int(v / 49.0)
        # Set the new value of the pixel
        mean_image.itemset((i, j), d)

# Show Image
cv2.imshow('salah/Average',  mean_image)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_Average.jpg',  mean_image)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Median Filter (we used it to remove noise)

# Read Image as gray scale
img2 = cv2.imread('noisy.jpg', 0)
median_image = img2.copy()

# Get the dimensions of the image
width_img = img2.shape[1]
height_img = img2.shape[0]

# Iterate of sub region of the image as i need to exclude the borders
for i in np.arange(3, height_img - 3):
    for j in np.arange(3, width_img - 3):
        # Initialize empty array of neighbors
        neighbor = []
        # Collect the neighbor pixel values for a pixel at position(i,j)
        # For each pixel i need to have 3 pixels its right, 3 pixels its left, 3 pixels above it, and 3 pixels below it
        for a in np.arange(-3, 4):
            for b in np.arange(-3, 4):
                # Get all the neighbors of the pixel at position(i,j)
                # It will iterate over the neighborhood of the pixel(i,j)
                e = img2.item(i + a, j + b)
                neighbor.append(e)
        neighbor.sort()
        # 7*7 = 49 of the neighborhood pixels
        # Divide 49-1 / 2 = 24 to get the median value
        median_filter = neighbor[24]
        f = median_filter
        # Set the new value of the pixel
        median_image.itemset((i, j), f)

# Show Image
cv2.imshow('noisy/Median', median_image)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\noisy_median.jpg', median_image)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Minimum Filter (Non-linear filter)

# Read Image as gray scale
img3 = cv2.imread('salah.png', 0)
minimum_image = img3.copy()

# Get the dimensions of the image
width_img = img3.shape[1]
height_img = img3.shape[0]

# Iterate of sub region of the image as i need to exclude the borders
for i in np.arange(3, height_img - 3):
    for j in np.arange(3, width_img - 3):
        # Initialize the minimum value with the greatest value of gray scale
        # Get the minimum intensity of pixel value
        min = 255
        # For each pixel i need to have 3 pixels its right, 3 pixels its left, 3 pixels above it, and 3 pixels below it
        for a in np.arange(-3, 4):
            for b in np.arange(-3, 4):
                g = img3.item(i + a, j + b)
                if g < min:
                    min = g
        h = min
        # Set the new value of the pixel
        minimum_image.itemset((i, j), h)

# Show Image
cv2.imshow('salah/Minimum', minimum_image)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_minimum.jpg', minimum_image)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Maximum Filter (Non-linear filter)

# Read Image as gray scale
img4 = cv2.imread('salah.png', 0)
maximum_image = img4.copy()

# Get the dimensions of the image
width_img = img4.shape[1]
height_img = img4.shape[0]

# Iterate of sub region of the image as i need to exclude the borders
for i in np.arange(3, height_img - 3):
    for j in np.arange(3, width_img - 3):
        # Initialize the maximum value with the lowest value of gray scale
        # Get the maximum intensity of pixel value
        max = 0
        # For each pixel i need to have 3 pixels its right, 3 pixels its left, 3 pixels above it, and 3 pixels below it
        for a in np.arange(-3, 4):
            for b in np.arange(-3, 4):
                k = img4.item(i + a, j + b)
                if k > max:
                    max = k
        l = max
        # Set the new value of the pixel
        maximum_image.itemset((i, j), l)

# Show Image
cv2.imshow('salah/Maximum', maximum_image)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_maximum.jpg', maximum_image)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Contrast Filter

# Read Image as gray scale
img5 = cv2.imread('salah.png', 0)

# Get the dimensions of the image
width_img = img5.shape[1]
height_img = img5.shape[0]
contrast = 2

# Iterate over the image
for i in np.arange(height_img):
    for j in np.arange(width_img):
        # Get the value of position(i,j)
        # Intensity value from 0 to 255
        m = img5.item(i, j)
        # Compute the value by multiplying the old value by the contrast coefficient
        n = math.ceil(m * contrast)
        # Compare the value if its value overshoots the maximum allowed value of 255
        if n > 255:
            n = 255
        # Set the new value of the pixel
        img5.itemset((i, j), n)

# Show Image
cv2.imshow('salah/Contrast', img5)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_contrast.jpg', img5)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Negative Filter

# Read Image as gray scale
img6 = cv2.imread('salah.png', 0)

# Get the dimensions of the image
width_img = img6.shape[1]
height_img = img6.shape[0]
# Maximum intensity of gray scale
high = 255

# Iterate over the image
for i in np.arange(height_img):
    for j in np.arange(width_img):
        # Get pixel value at position(i,j)
        o = img6.item(i, j)
        # Compute new value with maximum intensity minus the current value
        p = high - o
        # Set the new value of the pixel
        img6.itemset((i, j), p)

# Show Image
cv2.imshow('salah/Negative', img6)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_negative.png', img6)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Brightness Filter

# Read Image as gray scale
img7 = cv2.imread('salah.png', 0)

# Get the dimensions of the image
width_img = img7.shape[1]
height_img = img7.shape[0]
# Set parameter brightness
brightness = 80

# Iterate over the image
for i in np.arange(height_img):
    for j in np.arange(width_img):
        q = img7.item(i, j)
        # Increase intensity value by brightness
        r = q + brightness
        # Compare if it overshoots the maximum allowed then set it to 255 to make sure that it is in the allowed range
        if r > 255:
            r = 255
        # Set the new value of the pixel
        img7.itemset((i, j), r)

# Show Image
cv2.imshow('salah/Brightness', img7)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_brightness.jpg', img7)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------------------

# Apply Threshold Filter

# Read Image as gray scale
img8 = cv2.imread('salah.png', 0)

# Get the dimensions of the image
width_img = img8.shape[1]
height_img = img8.shape[0]
# Set threshold value
th = 100

# Iterate over the image
for i in np.arange(height_img):
    for j in np.arange(width_img):
        # Get current pixel at position(i,j)
        s = img8.item(i, j)
        # Compare if the current value is greater than threshold set it to the maximum value "255"
        if s > th:
            t = 255
        # If it is smaller than threshold set it to the minimum value "0"
        else:
            t = 0
        # Set the new value of the pixel
        img8.itemset((i, j), t)

# Show Image
cv2.imshow('salah/Threshold', img8)

# Write Image
cv2.imwrite(r'C:\Comp\4th YEAR\SECOND SEMESTER\SUBJECTS\IMAGE PROCESSING\Assignments\Assignment_1\images\salah_threshold.jpg', img8)

# Destroy Window
cv2.waitKey(0)
cv2.destroyAllWindows()
