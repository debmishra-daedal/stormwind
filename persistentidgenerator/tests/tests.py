import unittest
from unittest.mock import patch
from persistentidgen import seqguidgen as idgen


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
