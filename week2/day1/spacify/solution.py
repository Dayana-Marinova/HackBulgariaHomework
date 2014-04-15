from string_utils import tabs_to_spaces


def spacify(filename):
    new_file = open(filename, 'r')
    contents = new_file.read()
    contents = tabs_to_spaces(contents, 2)
    new_file.close()
    file = open(filename, 'w')
    file.write(contents)
    file.close()
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    return contents

print(spacify('studentss.txt'))
