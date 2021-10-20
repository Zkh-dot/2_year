# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    if len(args) == 1:
        for item in items:
            try:
                yield item[args[0]]
            except KeyError:
                return None
    else:
        for item in items:
            rez = {}
            for arg in args:
                try:
                    rez[arg] = item[arg]
                except KeyError: pass
            yield rez

if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(next(field(goods, 'title')))
    t = field(goods, 'title', 'price')
    print(next(t))
    print(next(t))
