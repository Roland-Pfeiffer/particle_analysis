#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton


def on_click(event):
    if event.button is MouseButton.LEFT:
        x, y = int(event.xdata), int(event.ydata)
        return x, y


def get_clicked_coordinates(fpath_img):
    img = cv2.imread(fpath_calibration)
    print(img.shape)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(img)
    binding_id = plt.connect('button_press_event', on_click)
    plt.show()
    print(type(binding_id))
    plt.disconnect(binding_id)


if __name__ == '__main__':
    fpath_calibration = '/media/findux/DATA/Code/particle_analysis/images/2400_dpi_size_calibration.png'
    get_clicked_coordinates(fpath_calibration)

