"""
Avoider-robot program for the Lego NXT.

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

if __name__ == '__main__':
	import random, sys
	gen = random.Random()

	turtle = nxt_turtle.LegoTurtle()
	while(True): 
		us_reading = turtle.get_ultrasound()
		while  us_reading > 15:
			print 'Moving forward...'
			turtle.forward(360 * 2) # 2 full rotations
			sleep(1)
		turtle.play_tone(LegoTurtle.FREQ_C)
		extent = gen.randint(0, 360) # closed interval
                if gen.choice([True, False]):
                    	print 'Turning', extent, 'degrees left...'
                    	turtle.left(extent)
                else:
                    	print 'Turning', extent, 'degrees right...'
                    	turtle.right(extent)
		sleep(0.3)
	print 'Closing socket to brick...'
	turtle.close()
        
