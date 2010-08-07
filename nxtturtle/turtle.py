#!/usr/bin/env python

"""
Logo-like interface to the Lego NXT robot.

Copyright (C) Sarah Mount, 2008.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

"""

import nxt.locator
from nxt.motor import *
from nxt.sensor import *
from time import sleep

__author__ = 'Sarah Mount <s.mount@wlv.ac.uk>'
__date__ = 'March 2008'

class LegoTurtle:
	"""Logo-like interface to the Lego NXT.
	"""
	
	WHEEL_POWER = 100 # Percentage power to apply to servo motors
	
	FREQ_C = 523
        FREQ_C_SHARP = 554
        FREQ_D_FLAT = FREQ_C_SHARP
	FREQ_D = 587
        FREQ_D_SHARP = 622
        FREQ_E_FLAT = FREQ_D_SHARP
	FREQ_E = 659
        FREQ_F = 699
        FREQ_F_SHAP = 740
        FREQ_G_FLAT = FREQ_F_SHARP
	FREQ_G = 784
        FREQ_G_SHARP = 831
        FREQ_A_FLAT = FREQ_G_SHARP
        FREQ_A = 880
        FREQ_A_SHARP = 932
        FREQ_B_FLAT = FREQ_A_SHARP
        FREQ_B = 988
        FREQ_C2 = 1047

	def __init__(self, sock=None):
            	if sock:
			self.sock = sock
                else:
			try:
				self.sock = nxt.locator.find_one_brick()
			except nxt.locator.BrickNotFoundError:
				print 'No NXT bricks found'
				sys.exit()
		self.brick = self.sock.connect()
		# Setup sensors
		self.touch = TouchSensor(self.brick, PORT_1)
		self.sound = SoundSensor(self.brick, PORT_2)
		self.light = LightSensor(self.brick, PORT_3)
		self.ultrasound = UltrasonicSensor(self.brick, PORT_4)
		# Setup motors
		self.wheel_l = Motor(self.brick, PORT_B)
		self.wheel_r = Motor(self.brick, PORT_C)
		return

	def __run_motor(self, l_fwd, r_fwd, l_rot, r_rot):
		# Set forward or backward motion for each wheel
		if l_fwd: l_power = LegoTurtle.WHEEL_POWER
		else: l_power = LegoTurtle.WHEEL_POWER * -1
		if r_fwd: r_power = LegoTurtle.WHEEL_POWER
		else: r_power = LegoTurtle.WHEEL_POWER * -1		
		# Left wheel
		self.wheel_l.power = l_power
		self.wheel_l.mode = MODE_MOTOR_ON
		self.wheel_l.run_state = RUN_STATE_RUNNING
		self.wheel_l.tacho_limit = l_rot
		self.wheel_l.set_output_state()
		# Right wheel
		self.wheel_r.power = r_power
		self.wheel_r.mode = MODE_MOTOR_ON
		self.wheel_r.run_state = RUN_STATE_RUNNING
		self.wheel_r.tacho_limit = r_rot
		self.wheel_r.set_output_state()
		return

	def forward(self, rotations):
            	"""Move the NXT forward by /rotations/ rotations of the wheels.
                """
		self.__run_motor(True, True, rotations, rotations)
		return

	def backward(self, rotations):
            	"""Move the NXT backward by /rotations/ rotations of the wheels.
                """
		self.__run_motor(False, False, rotations, rotations)
		return
	
	def left(self, degrees):
            	"""Turn the NXT left by /degrees/ degrees.
                """
		self.__run_motor(True, True, 0, degrees)
		return

	def right(self, degrees):
            	"""Turn the NXT right by /degrees/ degrees.
                """
		self.__run_motor(True, True, degrees, 0)
		return

	def close(self):
            	"""Close the Bluetooth / USB connection to the NXT.
                """
		self.sock.close()
		return

	def get_ultrasound(self):
            	"""Return the current reading from the ultrasound sensor.
                """
		return self.ultrasound.get_sample()

	def get_touch(self):
            	"""Return the current reading from the touch sensor.
                """
		if self.touch.get_sample():
			return True
		return False

	def get_sound(self):
            	"""Return the current reading from the sound sensor.
                """
		return self.sound.get_sample()

	def get_light(self):
            	"""Return the current reading from the light sensor.
                """
		return self.light.get_sample()

	def play_tone(self, freq, ms=500):
            	"""Play a note with frequency /freq/ for ms milleseconds.
                """
		self.brick.play_tone_and_wait(freq, ms)
		sleep(0.5)

