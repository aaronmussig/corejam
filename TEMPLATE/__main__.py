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

import argparse
import logging
import sys
import traceback
from gettext import gettext

from TEMPLATE import __version__, __title__, __url__
from TEMPLATE.exceptions import JAMException
from TEMPLATE.logging import colour
from TEMPLATE.logging import logger_setup


class ColoredArgParser(argparse.ArgumentParser):
    def print_usage(self, file=None):
        if file is None:
            file = sys.stdout
        lines = ['',
                 '  ' + colour(__title__, fg='blue') + ' ' + colour(f'v{__version__}', fg='cyan'),
                 f'  {__url__}',
                 ''
                 '\n']
        file.write('\n'.join(lines))

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        file.write(self.format_help()[0].upper() + self.format_help()[1:] + '\n')

    def exit(self, status=0, message=None):
        if message:
            sys.stderr.write(f"{colour(message, fg='red')}\n")
        sys.exit(status)

    def error(self, message):
        self.print_usage(sys.stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(2, gettext('[%(prog)s] Error: %(message)s\n') % args)

    def print_version(self):
        sys.stdout.write(f"{colour(__title__, fg='blue')} "
                         f"{colour(f'v{__version__}', fg='cyan')}\n")


def main_parser():
    parser = ColoredArgParser(prog=__title__)
    subparsers = parser.add_subparsers(dest='subparser_name')
    subparsers.metavar = 'methods'

    # define common shared arguments
    base_subparser = argparse.ArgumentParser(add_help=False)
    base_subparser.add_argument('--debug', help='output debugging information', action='store_true', default=False)

    # subparser a
    subparser_a = subparsers.add_parser('foo',
                                        help='foo help.',
                                        parents=[base_subparser])

    sa_mutex = subparser_a.add_argument_group('mutually exclusive required arguments')
    mutex_group = sa_mutex.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('--a',
                             help='add a.')

    subparser_b = subparsers.add_parser('bar',
                                        help='bar help.',
                                        parents=[base_subparser])
    subparser_b.add_argument('--b',
                             help='add b.')

    return parser


def main():
    parser = main_parser()

    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(1)
    elif sys.argv[1] in {'-v', '--v', '-version', '--version'}:
        parser.print_version()
        sys.exit(0)
    else:
        args = parser.parse_args()

        # setup logger
        logger_setup(args.out_dir if hasattr(args, 'out_dir') else None,
                     f'{__title__}.log', __title__, __version__, False,
                     hasattr(args, 'debug') and args.debug)
        log = logging.getLogger('default')
        warn_log = logging.getLogger('warnings')

        try:
            # Do something
            pass
            log.info('inf')
            log.warning('war')
            log.error('err')
            log.debug('debug')
        except SystemExit:
            log.error('Controlled exit resulting from early termination.')
            sys.exit(1)
        except KeyboardInterrupt:
            log.error('Controlled exit resulting from keyboard interrupt.')
            sys.exit(1)
        except JAMException as e:
            if len(str(e)) > 0:
                log.error('{}'.format(e))
            log.error('Controlled exit resulting from an unrecoverable error or warning (see warnings.log).')

            msg = 'Controlled exit resulting from an unrecoverable error or warning.\n\n'
            msg += '=' * 80 + '\n'
            msg += 'EXCEPTION: {}\n'.format(type(e).__name__)
            msg += '  MESSAGE: {}\n'.format(e)
            msg += '_' * 80 + '\n\n'
            msg += traceback.format_exc()
            msg += '=' * 80
            warn_log.info(msg)
            sys.exit(1)
        except Exception as e:
            if len(str(e)) > 0:
                log.error('{}'.format(e))
            log.error('Uncontrolled exit resulting from an unexpected error (see warnings.log).')
            msg = 'Controlled exit resulting from an unrecoverable error or warning.\n\n'
            msg += '=' * 80 + '\n'
            msg += 'EXCEPTION: {}\n'.format(type(e).__name__)
            msg += '  MESSAGE: {}\n'.format(e)
            msg += '_' * 80 + '\n\n'
            msg += traceback.format_exc()
            msg += '=' * 80
            warn_log.info(msg)
            sys.exit(1)

    # Done - no errors.
    sys.exit(0)


if __name__ == "__main__":
    main()
