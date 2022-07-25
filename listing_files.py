import os

folder = "DATA"

files_in_data = os.listdir(folder)

print(f"files_in_data: {files_in_data}\n")

text_files = [f for f in files_in_data if f.endswith('.txt')]
print(f"text_files: {text_files}\n")

print('-' * 60)

for entry in os.scandir(folder):
    if entry.name.endswith('.txt'):
        print(entry.name, entry.is_file(), entry.path)
        print(entry.stat(), '\n')

