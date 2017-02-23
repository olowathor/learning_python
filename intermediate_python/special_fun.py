'''
#Normal generator
#x = range(5)
x = (i for i in range(5))

next(x)
x.__next__()
'''

#First made generator
class range_examp:
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val

#x = range_examp(5)
x = (i for i in range_examp(5))
print(x.__next__())
print(next(x))

for i in x:
    print(i,i)

#Second made generator
def range_gen(end):
    current = 0
    while current < end:
        yield current
        current +=1

#x = range_gen(5)
x = (i for i in range_gen(5))
print(x.__next__())
print(next(x))


for i in x:
    print(i,i)
