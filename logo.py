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
#  logo.py
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

from random import choice

"""This module contains the logo and settings for its output."""

#
# Bash colors code
#
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN  = '\033[36m'
DEFAULT = '\033[00m'

#
# Logo
#
logo_P = ['  ___ ', '(  _ \\', ' )___/ ', '(__) ']
logo_R = [' ____ ', '(  _ \\', ')   / ', '(_)\\_)']
logo_D = [' ____', '(  _ \\', ')(_) )', ' (____/']

#
# Variable dpr function
#
def generate_random_dpr_string():
    """Return random (using random module from Python) vallue from array: ['prd','pdr','drp','dpr','rpd','rdp']"""
    var = ['prd','pdr','drp','dpr','rpd','rdp']
    return choice(var)

#    
# Settings function
#
def install_logo_settings(color_1 = RED, color_2 = YELLOW, color_3 = BLUE, order = 'prd'):
    """Returns a string-logo. The line is ready for output. Parameters: color_1 (check const, default = RED), color_2 (check const, default = YELLOW), color_3 (check const, default = BLUE), order (string: "prd", "drp", "pdr" etc.) """
    
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    if order == 'prd':
        first_line = f'{color_1}{logo_P[0]}{color_2}{logo_R[0]}{color_3}{logo_D[0]}\n'
        second_line = f'{color_1}{logo_P[1]}{color_2}{logo_R[1]}{color_3}{logo_D[1]}\n'
        third_line = f'{color_1}{logo_P[2]}{color_2}{logo_R[2]}{color_3}{logo_D[2]}\n'
        fourth_line = f'{color_1}{logo_P[3]}{color_2}{logo_R[3]}{color_3}{logo_D[3]}\n{DEFAULT}'
        
    elif order == 'pdr':
        first_line = f'{color_1}{logo_P[0]}{color_2}{logo_D[0]}{color_3}{logo_R[0]}\n'
        second_line = f'{color_1}{logo_P[1]}{color_2}{logo_D[1]}{color_3}{logo_R[1]}\n'
        third_line = f'{color_1}{logo_P[2]}{color_2}{logo_D[2]}{color_3}{logo_R[2]}\n'
        fourth_line = f'{color_1}{logo_P[3]}{color_2}{logo_D[3]}{color_3}{logo_R[3]}\n{DEFAULT}'

    elif order == 'drp':
        first_line = f'{color_1}{logo_D[0]}{color_2}{logo_R[0]}{color_3}{logo_P[0]}\n'
        second_line = f'{color_1}{logo_D[1]}{color_2}{logo_R[1]}{color_3}{logo_P[1]}\n'
        third_line = f'{color_1}{logo_D[2]}{color_2}{logo_R[2]}{color_3}{logo_P[2]}\n'
        fourth_line = f'{color_1}{logo_D[3]}{color_2}{logo_R[3]}{color_3}{logo_P[3]}\n{DEFAULT}'

    elif order == 'dpr':
        first_line = f'{color_1}{logo_D[0]}{color_2}{logo_P[0]}{color_3}{logo_R[0]}\n'
        second_line = f'{color_1}{logo_D[1]}{color_2}{logo_P[1]}{color_3}{logo_R[1]}\n'
        third_line = f'{color_1}{logo_D[2]}{color_2}{logo_P[2]}{color_3}{logo_R[2]}\n'
        fourth_line = f'{color_1}{logo_D[3]}{color_2}{logo_P[3]}{color_3}{logo_R[3]}\n{DEFAULT}'

    elif order == 'rpd':
        first_line = f'{color_1}{logo_R[0]}{color_2}{logo_P[0]}{color_3}{logo_D[0]}\n'
        second_line = f'{color_1}{logo_R[1]}{color_2}{logo_P[1]}{color_3}{logo_D[1]}\n'
        third_line = f'{color_1}{logo_R[2]}{color_2}{logo_P[2]}{color_3}{logo_D[2]}\n'
        fourth_line = f'{color_1}{logo_R[3]}{color_2}{logo_P[3]}{color_3}{logo_D[3]}\n{DEFAULT}'

    elif order == 'rdp':
        first_line = f'{color_1}{logo_R[0]}{color_2}{logo_D[0]}{color_3}{logo_P[0]}\n'
        second_line = f'{color_1}{logo_R[1]}{color_2}{logo_D[1]}{color_3}{logo_P[1]}\n'
        third_line = f'{color_1}{logo_R[2]}{color_2}{logo_D[2]}{color_3}{logo_P[2]}\n'
        fourth_line = f'{color_1}{logo_R[3]}{color_2}{logo_D[3]}{color_3}{logo_P[3]}\n{DEFAULT}'

    return '{0}{1}{2}{3}'.format(first_line, second_line, third_line, fourth_line)

if __name__ == "__main__":
    print(install_logo_settings(YELLOW,CYAN,MAGENTA,generate_random_dpr_string()))
