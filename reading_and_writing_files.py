

file_path = "DATA/mary.txt"

with open(file_path) as mary_in:
    for raw_line in mary_in:  #  "Mary had a little lamb;\n"
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("Normal:")
    print(contents, '\n')
    print("Raw:")
    print(repr(contents), '\n')
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)


