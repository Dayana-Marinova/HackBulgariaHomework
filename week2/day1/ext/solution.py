import os
import sys


def ext(extension):
    extension_length = len(extension)
    count = 0
    if '.' not in extension:
        return count
    for item in os.listdir("."):
        if item[-extension_length:] == extension:
            count += 1
    return count

#print(ext(sys.argv[1]))
