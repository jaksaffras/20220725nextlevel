import os   # includes os.path
from datetime import datetime

FOLDER = 'DATA'
FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"file_path: {file_path}")

dir_name = os.path.dirname(file_path)
print(f"dir_name: {dir_name}")

base_name = os.path.basename(file_path)
print(f"base_name: {base_name}")

abs_path = os.path.abspath(file_path)
print(f"abs_path: {abs_path}")

file_size = os.path.getsize(file_path)
print(f"file_size: {file_size}")

raw_file_mod_time = os.path.getmtime(file_path)
print(f"raw_file_mod_time: {raw_file_mod_time}")

file_mod_time = datetime.fromtimestamp(raw_file_mod_time)
print(f"file_mod_time: {file_mod_time}")

