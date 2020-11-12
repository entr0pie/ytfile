def read_file(your_file):
    file_obj = open(your_file, "r")
    lines = file_obj.readlines()
    valid = []
    for line in lines:
        line = line.replace("\n", "")
        if len(line) > 0:
            valid.append(line)

    return valid
