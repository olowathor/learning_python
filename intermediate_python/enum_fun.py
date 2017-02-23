import timeit

print(timeit.timeit('''
example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    (i, example[i])
''', number=50000))

print(timeit.timeit('''
example = ['left', 'right', 'up', 'down']

for i,j in enumerate(example):
    (i,j)
''', number=50000))

example = ['left', 'right', 'up', 'down']

new_dict = dict(enumerate(example))

[print(k,v) for k,v in new_dict.items()] 

