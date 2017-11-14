import os
import sys
import platform

"""
BSD 3-Clause License

Copyright (c) 2017, JimmyBot
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

def kb():

	""" This module checks for a specific strings using the systeminfo built-in-command """

	inputstring = input("Input a string(whatever you want, but intended to look for KBs for findstr to check against systeminfo\n-->  ")
	result = os.system('systeminfo | find "%s"' % inputstring)
	print(result)
	return kb

def winversion():

	"""
	This module returns the build of Windows that is currently running with platform, but it will
	probably work elsewhere.
	"""

	pltfrm = platform.platform()
	print("The following is your windows platform...As determined by platform.platform")
	print("-->  %s" % (pltfrm))
	return winversion

def boottime():
	uptime = os.system('systeminfo | find "System Boot Time"')
	return boottime

def main():

	""" This main module is the help command equivalent of pecan """

	print("The following commands are available thus far\n")
	print("--> winversion, kb, boottime\n")
	print("What command would you like to run?")
	command = input("-->  ")
	if (command == "winversion"):
		winversion()
	elif (command == "kb"):
		kb()
	elif (command == "uptime"):
		boottime()
	return main

main = main()
