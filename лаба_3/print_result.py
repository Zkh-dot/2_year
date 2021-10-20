def print_result(func):
    rez = func()
    print(str(func).split()[1])
    if type(rez) == list:
        for i in rez:
            print(i)
    elif type(rez) == dict:
        for i in rez:
            print(str(i) + " = " + str(rez[i]))
    else:
        print(rez)
    return lambda: rez

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
