#!/usr/bin/env python3

import configparser

import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

BORDER_WIDTH = 95
BORDER_WIDTH = 600
C = 0.01
BLOCK_SIZE = 15001
LOWER_INTENSITY_CUTOFF = 15
RESIZE_FACTOR = 0.1

fpath_particles = '/media/findux/DATA/Code/particle_analysis/images/1200_dpi_darkfield.png'
fpath_particles_w = '/media/findux/DATA/Code/particle_analysis/images/microplastics_01-white_test.png'

# Read img
img = cv2.imread(fpath_particles)

# Cut off the border
img = img[BORDER_WIDTH:-BORDER_WIDTH, BORDER_WIDTH:-BORDER_WIDTH]
print(img.shape)
height, width, _ = img.shape
height_resized = int(height * RESIZE_FACTOR)
width_resized = int(width * RESIZE_FACTOR)

# Convert to gray
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_bw = np.reshape(img_bw, (height, width, 1))
print(img_bw.shape)

# Binary masking
# binary_mask = cv2.adaptiveThreshold(img_bw, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, BLOCK_SIZE, C)
# Using conventional masking since i never got the adaptive thresholdin g to work properly (too few particles?)
binary_mask = cv2.threshold(img_bw, 20, 255, cv2.THRESH_BINARY)
plt.imshow(binary_mask[1])
plt.show()

# Image opening/closing
cv2.