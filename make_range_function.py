class Mygan():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        #  class.attibute will point to data which is in that class with that attibuter
        if Mygan.current < self.last:
            num = Mygan.current
            Mygan.current += 1
            return num
        raise StopIteration


gan = Mygan(0, 100)

for i in gan:
    print(i)
