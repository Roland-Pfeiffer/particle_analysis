#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt


def get_points(event):
    points = []
    for i in range(2):
        ix, iy = event.xdata, event.ydata
        points.append((ix, iy))
    fig.canvas.mpl_disconnect()
    return points


def on_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)



def calibrate_px_size(img_fpath):
    img = cv2.imread(img_fpath)
    print(img.shape)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
    coords = plt.ginput(3)
    plt.close()
    # cid = fig.canvas.mpl_connect('button_press_event', on_press)

    return coords



if __name__ == '__main__':
    fpath_particles = '/media/findux/DATA/Code/particle_analysis/images/microplastics_01-black.png'
    fpath_calibration = '/media/findux/DATA/Code/particle_analysis/images/2400_dpi_size_calibration.png'

    calibrate_px_size(fpath_calibration)