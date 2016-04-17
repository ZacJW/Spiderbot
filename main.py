#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  leg processing code.py
#  
#  Copyright 2016 Zachary <Zachary@ZAC-LAPTOP>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import math
def pythag3d(x, y, z):
	return math.sqrt((x**2)+(y**2)+(z**2))

def main(target_x, target_y, target_z):
	upper_leg_length = 8
	lower_leg_length = 8
	rot_1 = math.atan(target_y/target_x)
	print ("rotation 1")
	print (math.degrees(rot_1))
	dist = pythag3d(target_x, target_y, target_z)
	#print (dist)
	rot_2 = (math.asin(target_z/dist)+math.acos(((upper_leg_length**2)+(dist**2)-(lower_leg_length**2))/(2*upper_leg_length*dist)))
	print ("rotation 2")
	print (math.degrees(rot_2))
	rot_3 = math.acos(((upper_leg_length**2)+(lower_leg_length**2)-(dist**2))/(2*upper_leg_length*lower_leg_length))
	print ("rotation 3")
	print (math.degrees(rot_3))
	return 0

def globalToLocal(target_x, target_y, target_z, rot_x, rot_y, rot_z, pos_x, pos_y, pos_z):
	
	return 0
if __name__ == '__main__':
	import sys
	sys.exit(main(5, 6, -3))
	#sys.exit(main(sys.argv))
