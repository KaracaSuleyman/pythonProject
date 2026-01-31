



class New_Range:
    def __init__(self, start, end):
        self.start = start
        self.stop = end

    def __iter__(self):
        return self


    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        value = self.start
        self.start += 1
        return value



numbers=New_Range(2,29)
for i in numbers:
    print(i)
