import sqlite3
from pathlib import Path

# the_path = Path("cats")
# home_path = Path.home()
# print(the_path)
# print(Path.is_absolute(the_path))
# print(Path.is_absolute(home_path))

conn = sqlite3.connect('./files/sample.db', isolation_level="None")
#The connection stays open as long as the conn object exists and the script is running. When the script finishes, Python will close the connection automatically.


conn.execute("CREATE TABLE IF NOT EXISTS dogs(name TEXT, age INTEGER);")