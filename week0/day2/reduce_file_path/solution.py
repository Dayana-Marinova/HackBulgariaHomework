def reduce_file_path(path):
    new_path = path.split("/")
    result = []
    for item in new_path:
        if item == '..':
            result.pop()
        elif item == '.':
            pass
        elif item != '':
            result.append(item)
    return '/' + '/'.join(result)
