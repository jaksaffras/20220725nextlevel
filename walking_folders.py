import os

start_dir = '.'

folders_to_skip = ['.git', '.idea']

for current_directory, sub_directories, files in os.walk(start_dir):
    for folder in folders_to_skip:
        if folder in sub_directories:
            sub_directories.remove(folder)
    print(current_directory)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(current_directory, file_name)
            file_size = os.path.getsize(file_path)
            print(f"   {file_size:8d} {file_name}")


