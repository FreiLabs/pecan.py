def winversion():
    
#    import sys
    import platform

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
#    sysgetwin = sys.getwindowsversion()    
    print("The following is your windows platform...As determined by platform.platform")
    print("-->  %s" % (pltfrm))
#    print("The following is your windows version...As determined by sys.getwindowsversion")
#    print("-->  %s" % (sysgetwin))
    return winversion

winversion = winversion()

"""
All the sys parts are commented out because on python 3.6.2 they seemed to behave however they wanted rather than how I told them
"""
