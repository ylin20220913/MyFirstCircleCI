#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

class InvalidPinSelection(Exception):
    pass
class IncorrectOutputState(Exception):
    pass

class Device():
    # This library will be scoped to a test suite - one instance of it will be
    # used for all test cases in the test suite. This allows one connection to
    # be made and used in all test cases.
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    # Required to override API bindings in ATS.
    OVERRIDE = True

    """	Library for interacting with a device under test.

	This is a implementation of the rpi.GPIO lib. This Shim will provide the user control
	for all M7 IOs, when using an RPI.
	"""

    def __init__(self):
        self.input_pin = [17, 27, 23] #Relay 2, 3, 4 = Input 0, 1, 2
        self.output_enable = 4 #Input pin for verifying output on/off
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.output_enable, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.input_pin[0], GPIO.OUT) #2
        GPIO.setup(self.input_pin[1], GPIO.OUT) #3
        GPIO.setup(self.input_pin[2], GPIO.OUT) #4

    def turn_device_input_on(self, input):
        """ Turn an input on for the device under test.

        Example:
        | Turn device input on | input id |
        | Turn device input on | 0 |
        | Turn device input on | 1 |
        | Turn device input on | 2 |
        """
        if input == 0:
            pin = self.input_pin[0]
        elif input == 1:
            pin = self.input_pin[1]
        elif input == 2:
            pin = self.input_pin[2]
        else:
            raise InvalidPinSelection("Invalid pin selection, inputed pin is not a valid option")
        GPIO.output(pin, False)
        time.sleep(1)

    def turn_device_input_off(self, input):
        """ Turn an input off for the device under test.

        Example:
        | Turn device input off | input id |
        | Turn device input off | 0 |
        | Turn device input off | 1 |
        | Turn device input off | 2 |
        """
        if input == 0:
            pin = self.input_pin[0]
        elif input == 1:
            pin = self.input_pin[1]
        elif input == 2:
            pin = self.input_pin[2]
        else:
            raise InvalidPinSelection("Invalid pin selection, inputed pin is not a valid option")
        GPIO.output(pin, True)
        time.sleep(1)

    def turn_all_device_inputs_off(self):
        """ Turn all inputs off for the device under test.

        Example:
        | Turn all device inputs off |
        """
        GPIO.output(self.input_pin[0], True)
        GPIO.output(self.input_pin[1], True)
        GPIO.output(self.input_pin[2], True)
        time.sleep(1)

    def turn_all_device_inputs_on(self):
        """ Turn all inputs on for the device under test.

        Example:
        | Turn all device inputs on |
		"""
        GPIO.output(self.input_pin[0], False)
        GPIO.output(self.input_pin[1], False)
        GPIO.output(self.input_pin[2], False)
        time.sleep(1)

    def test_device_output_on(self):
        """ Check if the output is on. Raise exception if output is not on.

        Example:
        | Test device output on |
        """
        if (GPIO.input(self.output_enable)):
            pass
        else:
            raise IncorrectOutputState("Output is not in the correct state")

    def test_device_output_off(self):
        """ Check if the output is off. Raise exception if output is not off.

        Example:
        | Test device output off |
        """
        if (GPIO.input(self.output_enable)):
            raise IncorrectOutputState("Output is not in the correct state")
        else:
            pass
