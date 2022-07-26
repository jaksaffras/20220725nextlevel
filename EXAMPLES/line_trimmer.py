def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            # yield line.rstrip('\n\r')  # <1>
            yield line[:-1]

mary_in = trimmed('../DATA/mary.txt')
for trimmed_line in mary_in:
    print(trimmed_line)
print()

parrot_in = trimmed('../DATA/parrot.txt')
for line in parrot_in:
    print(line)
