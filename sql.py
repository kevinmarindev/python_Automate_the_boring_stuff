import sqlite3
from pathlib import Path

the_path = Path("cats")
home_path = Path.home()
print(the_path)
print(Path.is_absolute(the_path))
print(Path.is_absolute(home_path))