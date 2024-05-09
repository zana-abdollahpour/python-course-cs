# custom for loop
def my_for(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


my_for("ZhoZho", print)


# custom range()
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self): return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for n in Counter(50, 55):
    print(n)
