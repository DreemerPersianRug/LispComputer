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
#  prd.py
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

from serial.tools import list_ports
import serial
import logo
import info
import time

#
# Print random logo and info
#
logo_type = logo.generate_random_dpr_string()

print(logo.install_logo_settings(logo.RED, logo.YELLOW, logo.BLUE, logo_type))
print(info.head, info.description, info.istruction, info.exit) 

#
# BaundRate value
#
rate = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]

print(' Baundrate values:', logo.YELLOW, rate, logo.DEFAULT)

#
# Enter boundrate
#
baund_rate = 9600

while True:
	try:
		baund_rate = int(input(f'{logo.CYAN} baundRate> {logo.DEFAULT}'))
		count = False
		for i in rate:
			if baund_rate == i:
				count = True
				break

		if count == True:
			break
		else:
			print(' Please, enter number from \"Baundrate values\"!\n')
	except:
		print(' Please, enter number from \"Baundrate values\"!\n')

#
# Creating a list of ports
#
def portList():
	portList = []
	for p in list_ports.comports():
		portList.append(p.device)

	if len(portList) == 0:
		portList.append('Не найдено...')

	return portList

#
# Enter port
#
port_list = portList()
print('\n Portlist:', logo.MAGENTA, port_list , logo.DEFAULT)
print(' Enter \"update\" to update the portlist  or port name.\n')

port_name = ''

while True:
	try:
		port_name = str(input(f'{logo.BLUE} portName> {logo.DEFAULT}'))
		count = False
		for i in port_list:
			if (port_name == i) and (port_name != 'Не найдено...'):
				count = True
				break	
		if count == True:
			break
		if port_name == 'update':
			port_list = portList()
			print('\n Portlist:', logo.MAGENTA, port_list , logo.DEFAULT)
		else:
			print(' Please, enter value from \"Portlist\"!\n')
	except:
		print(' Please, enter value from \"Portlist\"!\n')

#
# Enter parametrs
#
print(f' \n Values:\n  [{logo.YELLOW}Baundrate{logo.DEFAULT}]: {baund_rate}\n  [{logo.CYAN}Portname{logo.DEFAULT}]: {port_name}\n')

#
# Create serial object
#
s = serial.Serial(port_name, baund_rate, timeout=1)
time.sleep(2)

#
# Create read and write func.
#

def onRead():
	data = [f'{logo.CYAN} uLISP -> {logo.DEFAULT}']
	while True:
		value = s.read()
		if value:
			data.append(value.decode('utf-8'))				
		else:
			break

	return ''.join(data)

def onWrite(data):
	s.write(bytes(data, 'utf-8'))

while True:
	try:
		value = onRead()
		print(logo.DEFAULT, value)
		onWrite(input(f'{logo.GREEN}>>>'))
	except:
		print(f'{logo.RED}>>> Please, check your device and reload {logo_type} soft!')
		s.close()
		break
