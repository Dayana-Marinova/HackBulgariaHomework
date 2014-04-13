import time
it_is_changed = False
name_of_file = ''


def create(list_of_names_file):
    stamp = time.strftime("%Y_%m_%d")
    global name_of_file
    global it_is_changed
    if not it_is_changed:
        name_of_file = 'attendance_' + stamp
        if len(list_of_names_file) == 0:
            list_of_names_file.append(name_of_file)
            output = 'New file created and loaded: %s' % name_of_file
            return output
        else:
            for name in range(0, len(list_of_names_file)):
                if list_of_names_file[name] == name_of_file:
                    output = 'You already have a file for today it is: %s' % name_of_file
                    return output
    else:
        list_of_names_file.append(name_of_file)
        output = 'New file created and loaded: %s' % name_of_file
        return output
    it_is_changed = False


def change_date(new_name, list_of_names_file):
    global it_is_changed
    global name_of_file
    if new_name not in list_of_names_file:
        name_of_file = new_name
        output = 'Date changed to %s.' % name_of_file + '\n' + 'Current file saved & discarded.' + '\n' + 'You can create or load.'
        it_is_changed = True
        return output
    else:
        output = "File with this name: %s is already exist for today too!" % new_name
        return output


def add(first_name, last_name, list_of_name_student, list_of_names_file):
    global it_is_changed
    global name_of_file
    name = first_name + ' ' + last_name + '\n'
    new_name = first_name + ' ' + last_name
    file = open('students.txt', 'r')
    if it_is_changed:
        list_of_name_student = []
    filename = open(name_of_file, 'a')
    if name in file:
        filename = open(name_of_file, 'r')
        if name in filename:
            output = '%s is already added to the list for today.' % new_name
            return output
        else:
            filename = open(name_of_file, 'a')
            if len(list_of_name_student) == 0:
                list_of_name_student.append(name)
                filename.writelines(new_name + '\n')
                output = '%s is now attending' % new_name
                return output
            elif name in list_of_name_student:
                output = '%s is already added to the list for today.' % new_name
                return output
            else:
                list_of_name_student.append(name)
                output = '%s is now attending' % new_name
                filename.writelines(new_name + '\n')
                return output
    else:
        output = 'This student does not exist!'
        return output


def lists(list_of_names_file):
    for file_name in range(0, len(list_of_names_file)):
        output = '[' + str(file_name + 1) + ']' + list_of_names_file[file_name]
        print(output)
    return len(list_of_names_file)


def load(index_of_file, list_of_names_file):
    global name_of_file
    for index in range(0, len(list_of_names_file)):
        if index_of_file == str(index + 1):
            name_of_file = list_of_names_file[index]
            output = 'File %s loaded' % list_of_names_file[index]
            return output
        else:
            return 'There is no list with that index'


def status():
    global name_of_file
    file = open(name_of_file, 'r')
    content = file.read()
    file.close()
    return content


def statistic(list_of_names_file):
    count = 0
    for name in list_of_names_file:
        file = open(name, 'r')
        for line in file:
            count += 1
        output = 'File: %s - %s people attending from total of 45 students' % (name, count)
        print(output)
        result = count
        count = 0
    return result


def main():
    list_of_names_file = []
    list_of_name_student = []
    while True:
        command = input("Enter command> ")
        command_array = command.split(" ")
        if command_array[0] == 'create':
            print(create(list_of_names_file))
        elif command_array[0] == 'change_date':
            print(change_date(command_array[1], list_of_names_file))
        elif command_array[0] == 'add':
            print(add(command_array[1], command_array[2], list_of_name_student, list_of_names_file))
        elif command_array[0] == 'list':
            lists(list_of_names_file)
        elif command_array[0] == 'load':
            print(load(command_array[1], list_of_names_file))
        elif command_array[0] == 'status':
            print(status())
        elif command_array[0] == 'statistic':
            statistic(list_of_names_file)
        elif command_array[0] == 'finish':
            break
        else:
            output = 'There is no command like this!'
            print(output)
            return output


if __name__ == '__main__':
    main()
