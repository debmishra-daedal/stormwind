# MIT License
#
# Copyright (c) 2024 Your Name
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sqlite3, sys, os, io, contextlib

sys.path.append("..")
from seqguidgen import domainSet, defLoc, dbPath, tableList
from seqguidgen import squerySavedID, uquerySavedID, iquerySavedID
from seqguidgen import iquerydroppedID, squerydroppedIDs, squerydroppedIDt


class guidgen:
    def __init__(self):
        self.numid = 1_000_000_000
        if dbPath is not None:
            self.fPath = dbPath
        else:
            self.fPath = defLoc
        self.stdout_stream = io.StringIO()
        self.stderr_stream = io.StringIO()

    # Create a sqlite database to store sql ids
    def create_database(self):
        with contextlib.redirect_stdout(self.stdout_stream), contextlib.redirect_stderr(
            self.stderr_stream
        ):
            dbName = self.fPath + "sqlidstore.db"
            if not os.path.exists(dbName):
                sys.stdout.write(f"Creating new database at {dbName}.\n")
                try:
                    conn = sqlite3.connect(dbName)
                    sys.stdout.write(
                        f"successfully connected to the database stored at {dbName}\n"
                    )
                    return conn
                except sqlite3.Error as e:
                    sys.stderr.write(f"Error connecting database:{e}\n")
            else:
                sys.stdout.write(
                    f"Database already present at {dbName}. Connecting to existing database\n"
                )
                try:
                    conn = sqlite3.connect(dbName)
                    sys.stdout.write(
                        f"successfully connected to the database stored at {dbName}\n"
                    )
                    return conn
                except sqlite3.Error as e:
                    sys.stderr.write(f"Error connecting database:{e}\n")

    # Check if the table exist
    def table_exists(self, tableName):
        with contextlib.redirect_stdout(self.stdout_stream), contextlib.redirect_stderr(
            self.stderr_stream
        ):
            conn = guidgen().create_database()
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tableName}'\n"
            )
            res = cursor.fetchone()
            conn.close()
            return res

    def create_table(self):
        with contextlib.redirect_stdout(self.stdout_stream), contextlib.redirect_stderr(
            self.stderr_stream
        ):
            for t in tableList:
                res = guidgen().table_exists(t)
                if res is None:
                    conn = guidgen().create_database()
                    cursor = conn.cursor()
                    cursor.execute(tableList[t])
                    conn.commit()
                    conn.close()
                    sys.stdout.write(f"table {t} created\n")
                else:
                    sys.stdout.write(f"table {t} already exists\n")

    # Generate an unique ID that can be used across
    def generate_id(self, cat="oth"):
        with contextlib.redirect_stdout(self.stdout_stream), contextlib.redirect_stderr(
            self.stderr_stream
        ):
            guidgen().create_table()
            conn = guidgen().create_database()
            cursor = conn.cursor()
            try:
                catval = domainSet[cat]
                cursor.execute(squerySavedID, (cat,))
                numericId = cursor.fetchone()
                if numericId is None:
                    self.numericId = domainSet[cat] * self.numid + 1
                    cursor.executemany(
                        iquerySavedID,
                        [
                            (cat, self.numericId),
                        ],
                    )
                else:
                    limit = (catval + 1) * self.numid
                    sys.stdout.write(catval + 1, self.numid)
                    if numericId[0] < limit:
                        self.numericId = numericId[0] + 1
                        cursor.execute(uquerySavedID, (self.numericId, cat))
                    else:
                        sys.stderr.write(
                            f"the latest master id {numericId} is already at limit of {limit}. Can't add a new one. Program will exit.\n"
                        )
                        sys.exit(1)
                conn.commit()
                conn.close()
                self.category = cat
                return self
            except KeyError:
                sys.stderr.write(f"Key {cat} not found in dictionary")
                sys.exit(1)

    # Once a master id is removed, it has to go to the droppedID table. So that it can be reused
    def drop_id(self, id, cat="oth"):
        with contextlib.redirect_stdout(self.stdout_stream), contextlib.redirect_stderr(
            self.stderr_stream
        ):
            guidgen().create_table()
            conn = guidgen().create_database()
            cursor = conn.cursor()
            cursor.execute(squerydroppedIDs, (cat,))
            vals = cursor.fetchone()
            cursor.execute(squerydroppedIDt, (cat, id))
            valt = cursor.fetchone()
            if vals is None:
                sys.stderr.write(
                    "There is no entries in the savedID table. Redundant drop request\n"
                )
            elif vals[0] < id:
                sys.stderr.write(
                    f"Input value {id} is higher than lastest value {val[0]}. Redundant drop request\n"
                )
            elif valt is not None:
                sys.stderr.write(
                    f"the value {id} and category {cat} combinations is already dropped.\n"
                )
            else:
                cursor.execute(iquerydroppedID, (cat, id))
            conn.commit()
            conn.close()

    # Log output and errors
    def logger(self):
        stdout_log = self.stdout_stream.getvalue()
        stderr_log = self.stderr_stream.getvalue()
        return self
