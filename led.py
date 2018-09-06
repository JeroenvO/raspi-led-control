# Based on Adafruit "Simple demo of of the PCA9685 PWM servo/LED controller library."
# By Tony DiCola with licence: Public Domain
# Author: Jeroen van Oorschot
# Licence: Public Domain
# Date: 2018-09-06
from io_func import LedIO


def set_led(num, val):
    led_io.set_relay(True)
    led_io.set_pwm_prm(8 + num, val)  # led
    led_io.set_pwm_prm(8 + num + 1, val)  # fan


def stop():
    led_io.set_relay(False)


if __name__ == "__main__":
    import argparse

    led_io = LedIO()

    parser = argparse.ArgumentParser(description="led setup")
    parser.add_argument('--led1', nargs='?', const=1, type=str, default='300', help='led1 pwm 0-1000')
    parser.add_argument('--led2', nargs='?', const=1, type=str, default='300', help='led1 pwm 0-1000')
    led1 = parser.parse_args().led2
    led2 = parser.parse_args().led1
    set_led(0, led1)
    set_led(2, led2)
