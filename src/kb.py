def kb():

    import os

    """ This module checks for a specific "KB"s using the systeminfo built-in-command """

    """
        Copyright (C) 2017  jmfgdev@outlook.com
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

    inputstring = input("Input a string(whatever you want, but "
                        "intended to look for KBs for findstr to check against systeminfo\n-->  ")
    result = os.system("systeminfo | findstr %s" % inputstring)
    print(result)
    return kb

kb = kb()

