###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

from corejam import __title__, __version__, __url__
from corejam.argparse import CustomArgParser, jam_parser


def main_parser():
    parser = CustomArgParser(prog=__title__, ver=__version__, url=__url__)
    return parser


def main():
    with jam_parser(main_parser(), __title__, __version__) as _:
        pass


if __name__ == "__main__":
    main()
