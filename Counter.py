class Counter:

    def __init__(self, start):
        self.start = start
        print(self.start)

    def increment(self):
        self.start += 1
        print(self.start)


my_counter = Counter(5)


my_counter.increment()
