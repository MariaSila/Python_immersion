import argparse


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('-number', type=int, help='Integer number')
parser.add_argument('-text', type=str, help='Any text')
parser.add_argument('-v', '--verbose', action='store_true', help='If used, additional help is displayed')
parser.add_argument('-r', '--repeat', type=int, default=1, help='Specifies how many times to repeat a line in the output')
args = parser.parse_args()
# print(args)


def func(num: int, txt: str):
    return txt * num


if __name__ == '__main__':
    if args.verbose:
        print('Repeating the text the specified number of times')
    elif args.repeat:
        for i in range(args.repeat):
            print(func(args.number, args.text))
    else:
        print(func(args.number, args.text))
