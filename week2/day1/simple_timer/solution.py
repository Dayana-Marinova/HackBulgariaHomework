is_started = False
time_left = 0
is_finish = False


def start_timer(seconds):
    global is_started
    global time_left
    if not is_started:
        is_started = True
        time_left = seconds
        return True
    return False


def decrease_time():
    global time_left
    if not is_started or time_left == 0:
        return False
    time_left -= 1
    return True


def is_timer_running():
    global is_started
    global time_left
    if is_started and time_left > 0:
        return True
    return False


def stop_timer():
    global is_started
    global is_finish
    if is_started:
        is_started = False
        is_finish = True
        return True
    return False


def seconds_left():
    global time_left
    global is_started
    global is_finish
    if is_finish or not is_started:
        return 0
    return time_left
