# Copyright (c) 2024 Deb Mishra
# This file is part of persistentidgenerator
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import unittest, sys
from unittest.mock import patch

sys.path.append("../..")
import persistentidgenerator.seqguidgen as idgen


class Testpersistentidgen(unittest.TestCase):

    # Generrate guid for any of the listed entities
    def test_happyflow1_generateguid(self):
        val = idgen.guidgen().generate_id("fx")
        guid = val.numericId
        self.assertIsNotNone(guid)

    # Generrate guid for any of the default entity
    def test_happyflow2_generateguid_def(self):
        val = idgen.guidgen().generate_id()
        guid = val.numericId
        self.assertIsNotNone(guid)

    # Don't generate guid for entries other than provided dictionary pairs
    # @patch("sys.exit")
    # def test_unhappyflow1_generateguid(self, mock_exit):
    #     with self.assertRaises(SystemExit) as cm:
    #         val = idgen.guidgen().generate_id("rand")
    #     self.assertEqual(cm.exception.code, 1)
    #     mock_exit.assert_called_with(1)


# if __name__ == "__main__":
#     unittest.main()


# guidgen().create_table()
# val = guidgen().generate_id()
# print(val.numericId, val.category)
# dval = guidgen().drop_id(4, "oth")
# conn = guidgen().create_database()
# cursor = conn.cursor()
# query = "DROP TABLE IF EXISTS droppedID"
# try:
#     cursor.execute(query)
#     conn.commit()
#     conn.close()
# except sqlite3.Error as e:
#     print("error dropping the table:\n", e)
