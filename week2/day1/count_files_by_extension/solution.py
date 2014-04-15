import os


def ext(folder, extension):
    extension_length = len(extension)
    count = 0
    if '.' not in extension:
        return count
    for path in os.listdir(folder):
        if path[-extension_length:] == extension:
            count += 1
    return count
