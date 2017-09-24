import os
import sys
import platform

def kb():

	""" This module checks for a specific "KB"s using the systeminfo built-in-command """

	"""
	Copyright (C) 2017  jmfgdev
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published
	by the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.
	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.
	"""

	inputstring = input("Input a string(whatever you want, but intended to look for KBs for findstr to check against systeminfo\n-->  ")
	result = os.system("systeminfo | findstr %s" % inputstring)
	print(result)
	return kb

def winversion():

	""" 
	This module returns the build of Windows that is currently running with platform, but it will 
	probably work elsewhere.
	"""

	"""
	Copyright (C) 2017  jmfgdev
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published
	by the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.
	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.
	"""
	
	pltfrm = platform.platform()
	print("The following is your windows platform...As determined by platform.platform")
	print("-->  %s" % (pltfrm))
	return winversion

def main():

	""" This main module is the help command equivalent of pecan """

	"""
	Copyright (C) 2017  jmfgdev
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published
	by the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.
	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.
	"""

	print("The following commands are available thus far\n")
	print("--> winversion, kb")
	print("What command would you like to run?")
	command = input("-->  ")
	if (command == "winversion"):
		winversion()
	elif (command == "kb"):
		kb()
	return main

main = main()
