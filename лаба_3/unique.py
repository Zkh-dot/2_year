# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        try:
            self.ignore_case = kwargs["ignore_case"]
        except KeyError:
            self.ignore_case = False
        self.items_uniq_it = iter(set(items))
        if self.ignore_case:
            self.finded = {}
            item = next(self.items_uniq_it)
            if item.lower() not in self.finded:
                self.finded[item.lower()] = item
            self.keys = iter(self.finded)


    def __next__(self):
        if not self.ignore_case:
            return next(self.items_uniq_it)
        return self.finded[next(self.keys)]



    def __iter__(self):
        return self

if __name__ == "__main__":
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    t = Unique(data)
    for i in t:
        print(i)
