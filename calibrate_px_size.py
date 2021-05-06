#!/usr/bin/env python3

import configparser
import math

import cv2
import matplotlib.pyplot as plt
import numpy as np


def get_click_coordinates(img: np.ndarray, title):
    """Records and returns two coordinates on user click.
    Returns a tuple of point coordinate tuples:
    ((pt1_x, pt1_y), (pt2_x, pt2_y))"""
    fig, ax = plt.subplots()
    mng = plt.get_current_fig_manager()
    mng.set_window_title(title)
    ax.imshow(img)
    coords = plt.ginput(2)  # record two clicks, then continue.
    plt.close(fig)
    return coords


def enter_distance():
    """Receives numerical user input."""
    while True:
        distance_ui = input('Enter known distance between previously selected points (in mm):\n > ')
        try:
            distance = int(distance_ui)
        except ValueError:
            print('Please enter a number!')
            continue
        else:
            return distance


def get_px_size(img: np.ndarray, title=None):
    """Takes a tuple of two points () and a distance between them in mm.
    Returns the pixel size (in mm) calculated from this distance."""
    _coordinates = get_click_coordinates(img, title=title)
    _distance_mm = enter_distance()
    _delta_x = _coordinates[1][0] - _coordinates[0][0]
    _delta_y = _coordinates[1][1] - _coordinates[0][1]
    _distance_px = math.sqrt((_delta_x ** 2) + (_delta_y ** 2))  # Pythagoras
    mm_per_px = _distance_mm / _distance_px
    return mm_per_px


def calibrate_px_size(fpath_calib_img, fpath_cfg_file='calibration.cfg'):
    img = cv2.imread(fpath_calib_img)
    px_size_vertical = get_px_size(img, title='Vertical')
    px_size_horizontal = get_px_size(img, title='Horizontal')
    print(px_size_vertical)
    print(px_size_horizontal)

    config = configparser.ConfigParser()
    config['PX_CALIBRATION'] = {'mm_per_px_vert': str(px_size_vertical),
                                'mm_per_px_horz': str(px_size_horizontal)}
    with open(fpath_cfg_file, 'w') as cfg:
        config.write(cfg)


if __name__ == '__main__':
    fpath_particles = '/media/findux/DATA/Code/particle_analysis/images/microplastics_01-black.png'
    fpath_calibration = '/media/findux/DATA/Code/particle_analysis/images/2400_dpi_size_calibration.png'

    calibrate_px_size(fpath_calibration)