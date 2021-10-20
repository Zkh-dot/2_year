data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

def result(lamb):
    if lamb == 0:
        return sorted(data, reverse = True)
    else:
        return sorted(data, key=lambda x: -x)

if __name__ == '__main__':
    print(result(0))
    print(result(1))
