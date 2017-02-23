names = ['Jeff', 'Gary', 'Jill', 'Samantha']

[print ('Hello there, ' + name) for name in names]
[print (' '.join(['Hello there, ', name])) for name in names]

import os

loc_of_files = str(os.getcwd()) #'/home/olowathor/Dokumenty/Python/sentdex/intermediate_python'
file_name = 'strings_fun.py'

print(loc_of_files + '/'  + file_name)

with open(os.path.join(loc_of_files,file_name)) as f:
    print(f.read())


who = 'Gary'
num = 12

print('{} bought {} apples today!'.format(who, num))
