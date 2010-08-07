"""
Play scales on the Lego NXT.

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

import nxt_turtle

__author__ = 'Sarah Mount <s.mount@wlv.ac.uk>'
__date__ = 'March 2008'

def play_scale(turtle):
        turtle.play_tone(LegoTurtle.FREQ_C)
        turtle.play_tone(LegoTurtle.FREQ_D)
        turtle.play_tone(LegoTurtle.FREQ_E)
        turtle.play_tone(LegoTurtle.FREQ_F)
        turtle.play_tone(LegoTurtle.FREQ_G)
        turtle.play_tone(LegoTurtle.FREQ_A)
        turtle.play_tone(LegoTurtle.FREQ_B)
        turtle.play_tone(LegoTurtle.FREQ_C2)


def play_chromatic(turtle):
        turtle.play_tone(LegoTurtle.FREQ_C)
        turtle.play_tone(LegoTurtle.FREQ_D_FLAT)
        turtle.play_tone(LegoTurtle.FREQ_D)
        turtle.play_tone(LegoTurtle.FREQ_E_FLAT)        
        turtle.play_tone(LegoTurtle.FREQ_E)
        turtle.play_tone(LegoTurtle.FREQ_F)
        turtle.play_tone(LegoTurtle.FREQ_G_FLAT)
        turtle.play_tone(LegoTurtle.FREQ_G
        turtle.play_tone(LegoTurtle.FREQ_A_FLAT)
        turtle.play_tone(LegoTurtle.FREQ_A)
        turtle.play_tone(LegoTurtle.FREQ_B_FLAT)
        turtle.play_tone(LegoTurtle.FREQ_B)
        turtle.play_tone(LegoTurtle.FREQ_C2)


if __name__ == '__main__':
	import time
	turtle = nxt_turtle.LegoTurtle()
	play_scale(turtle)
        time.sleep(1)
	play_chromatic(turtle)
	turtle.close()

