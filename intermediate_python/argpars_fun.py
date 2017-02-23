import argparse
import sys


def main():
    # usage: python argpars_fun.py --x=10 --y=2 --operation=mul

    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float, default = 1.0,
                        help = 'What is the first number?')
    parser.add_argument('--y', type=float, default = 1.0,
                        help = 'What is the second number?')
    parser.add_argument('--operation', type=str, default = 'add',
                        help = 'What operation? (add, sub, mul, div)')

    args = parser.parse_args()
    output = str(calc(args)) + '\n'
    sys.stdout.write(output)
    
def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()
'''
operation = calc(7,3,'div')
print(operation)
'''
