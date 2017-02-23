import timeit
#print(timeit.timeit('1+3', number=5000000))

'''
def div_by_five(num):
    if num % 5 == 0:
        return True
    return False

input_list = range(100)
'''
print(timeit.timeit('''
import div_by

input_list = range(100)

xyz = (i for i in input_list if div_by_five(i))
''', number=50000))


print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    return False

xyz = (i for i in input_list if div_by_five(i))
''', number=50000))

print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    return False


xyz = [i for i in input_list if div_by_five(i)]
''', number=50000))

print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    return False

xyz = list(i for i in input_list if div_by_five(i))
''', number=50000))

