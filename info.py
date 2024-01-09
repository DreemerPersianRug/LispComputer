#
#  ___  ____  ____  
#(  _ \(  _ \(  _ \
# )___/ )   / )(_) )
#(__)  (_)\_)(____/
#
# Created by PR&DTeam. 
# Sorry, we don't know English =) (we tried hard)
# Beta version 0.1
#
# -*- coding: utf-8 -*-
#
#  info.py
#  
#  Copyright 2023 PR&DTeam 
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

head = ' Welcome to a simple console utility for communicating over a serial port!\n'
description = 'The utility will allow you to communicate with your \033[36mMicroPC\033[00m.\n'
istruction = 'Please enter \033[33mbaundrate\033[00m and \033[35mport\033[00m!\n'
exit = 'Use \"ctrl + c\" or \"ctrl+z\" to exit.\n'

if __name__ == "__main__":
	print(head, description, istruction, exit) 
