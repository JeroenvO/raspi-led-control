# Author: Jeroen van Oorschot
# Licence: Public Domain
# Date: 2018-09-06

import RPi.GPIO as GPIO

import Adafruit_PCA9685 as af
from time import sleep


class LedIO:
    def __init__(self):
        # init rpi GPIO
        GPIO.setmode(GPIO.BCM)  # use BCM numbering
        GPIO.setup(22, GPIO.OUT)

        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = af.PCA9685()
        self.pwm.set_pwm_freq(500)  # hz freq of pwm

    @staticmethod
    def sanitize_int(x):
        if x < 0:
            return 0
        elif x > 4095:
            return 4095
        else:
            return int(x)

    def set_relay(self, on):
        """
        Set the 230v switch relay
        make sure outputs are disabled before switching

        :param mode:
        :return:
        """
        self.set_pwm_off()
        sleep(1)
        GPIO.output(22, on)
        sleep(1)

    def set_pwm_pct(self, channel, val):
        """
        set pwm in percent
        """
        val *= 40.96
        val = self.sanitize_int(val)
        self.pwm.set_pwm(channel, 0, val)

    def set_pwm_prm(self, channel, val):
        """
        set pwm in promile
        """
        val *= 4.096
        val = self.sanitize_int(val)
        self.pwm.set_pwm(channel, 0, val)

    def set_pwm_off(self):
        self.pwm.set_all_pwm(0, 0)
