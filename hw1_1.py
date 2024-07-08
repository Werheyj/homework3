calls = 0


def count_calls():
    global calls
    calls += 1
    print(calls)


def string_info(string):
    my_string_ = (len(string), string.upper(), string.lower())
    my_tuple = tuple(my_string_)
    print(my_tuple)
    count_calls()


def is_contains(str_, list_):
    my_list = []
    for i in list_:
        my_list.append(i.lower())
    if str_.lower() in my_list:
        print(True)
    else:
        print(False)
    count_calls()
