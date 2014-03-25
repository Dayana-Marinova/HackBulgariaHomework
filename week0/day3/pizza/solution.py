from time import time
from datetime import datetime


it_is_saved = False


def take(name, price, orders):
    if name in orders:
        orders[name] += float(price)
    else:
        orders[name] = float(price)
    output = "Taking order from %s for %s" % (name, price)
    print(output)
    return output


def status(orders):
    for key in orders:
        print(key + ' - ' + str(orders[key]))
    return len(orders)


def save(orders, list_of_orders):
    global it_is_saved
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    name_of_order = 'orders_' + stamp
    list_of_orders.append(name_of_order)
    file = open(stamp, 'w')
    for key in orders:
        file.write(key + " - " + str(orders[key]) + '\n')
    file.close()
    output = 'Saved the current order to %s.' % name_of_order
    print(output)
    it_is_saved = True
    return output


def lists(list_of_orders):
    for items in range(0, len(list_of_orders)):
        print('[' + str(items + 1) + ']' + list_of_orders[items])
    return len(list_of_orders)


def load(number, list_of_orders, it_is_saved):
    if it_is_saved:
        print('la')
        for order in range(0, len(list_of_orders)):
            if str(order + 1) == number:
                list_of_orders.remove(list_of_orders[order])
                return len(list_of_orders)
    else:
        output = 'You have unsaved order.' + '\n' + 'If you wish to discard the current order, type load again'
        print(output)
        return output


def finish(it_is_saved):
    if it_is_saved:
        print('Finishing order. Goodbye!')
        return 'Finishing order. Goodbye!'
    else:
        print('You have not saved your order.' + '\n' + 'If you wish to continue, type finish again.' + '\n' + 'If you want to save your order, type save')
        it_is_saved = True
        return 'You have not saved your order.' + '\n' + 'If you wish to continue, type finish again.' + '\n' + 'If you want to save your order, type save'


def main():
    global it_is_saved
    orders = {}
    list_of_orders = []
    while True:
        command = input("Enter command> ")
        command_array = command.split(" ")
        if command_array[0] == 'take':
            take(command_array[1], command_array[2], orders)
            it_is_saved = False
        elif command_array[0] == 'status':
            status(orders)
        elif command_array[0] == 'save':
            save(orders, list_of_orders)
        elif command_array[0] == 'list':
            lists(list_of_orders)
        elif command_array[0] == 'load':
            load(command_array[1], list_of_orders, it_is_saved)
        elif command_array[0] == 'finish':
            if not it_is_saved:
                finish()
            else:
                finish()
                break
        else:
            print('There is no command like this!')

if __name__ == '__main__':
    main()
