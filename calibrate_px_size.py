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


def px_ratio(px_size_x, px_size_y):
    ratio = px_size_x / px_size_y
    return ratio


def calibrate_px_size(fpath_calib_img, fpath_cfg_file='settings.cfg'):
    img = cv2.imread(fpath_calib_img)
    px_size_vertical = get_px_size(img, title='Vertical')
    px_size_horizontal = get_px_size(img, title='Horizontal')
    print(px_size_vertical)
    print(px_size_horizontal)
    ratio = px_ratio(px_size_horizontal, px_size_vertical)
    print(f'x/y ratio: {ratio}')

    # Produce a warning if the horizontal pixel size deviates by more than 20% of the vertical one.
    if abs(1 - ratio) > 0.2:  # the same as this -> if ratio > 1.2 or ratio < 0.8
        print(f'[WARNING]\tPixel size ratio (x/y): {ratio}')

    input('Press [Enter] to overwrite settings.cfg file.')
    # Initiate configparser
    config = configparser.ConfigParser()
    config.read(fpath_cfg_file)  # Read the full file so that the other sections are not lost
    # Overwrite the cgf file
    with open(fpath_cfg_file, 'w') as cfg:
        config['PX_CALIBRATION'] = {'mm_per_px_vert': str(px_size_vertical),
                                    'mm_per_px_horz': str(px_size_horizontal)}
        config.write(cfg)


if __name__ == '__main__':
    fpath_calibration = '/media/findux/DATA/Code/particle_analysis/images/1200_dpi_darkfield_calibration.png'
    calibrate_px_size(fpath_calibration)
