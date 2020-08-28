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

import os
import shutil
import tempfile
import unittest

from corejam.io import assert_path_exists


class TestIO(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix='corejam_test_')

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_assert_path_exists(self):
        self.assertRaises(OSError, assert_path_exists, '/dev/null')
        dir_todo = os.path.join(self.tmp_dir, 'foo')
        self.assertFalse(os.path.isdir(dir_todo))
        assert_path_exists(dir_todo)
        self.assertTrue(os.path.isdir(dir_todo))


if __name__ == '__main__':
    unittest.main()
