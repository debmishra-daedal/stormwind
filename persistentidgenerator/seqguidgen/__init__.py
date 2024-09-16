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

# -----------------------------Program to generate sequential ids ---------------
import os

# Create variables that can be used across the module
domainSet = {
    "fx": 1,
    "hp": 2,
    "sec": 3,
    "idx": 4,
    "bmrk": 5,
    "hld": 6,
    "por": 7,
    "ent": 8,
    "oth": 0,
}
defLoc = "./"
dbPath = os.getenv("SLITE_DB_PATH")
createQuery = """CREATE TABLE IF NOT EXISTS savedID (
    category VARCHAR(20) PRIMARY KEY UNIQUE,
    last_value BIGINT)"""
droppedQuery = """CREATE TABLE IF NOT EXISTS droppedID (
    id INTEGER PRIMARY KEY,
    category VARCHAR(20),
    dropped_value BIGINT)"""
tableList = {"savedID": createQuery, "droppedID": droppedQuery}
squerySavedID = "select last_value from savedID where category=?"
uquerySavedID = "update savedID set last_value = ? where category=?"
iquerySavedID = "insert into savedID (category, last_value) values (?,?)"
iquerydroppedID = "insert into droppedID (category, dropped_value) values (?,?)"
squerydroppedIDs = "select last_value from savedID where category=?"
squerydroppedIDt = "select 1 from droppedID where category=? and dropped_value=?"
