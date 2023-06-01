#!/usr/bin/env python

from gendiff.diff_with_formatter import generate_diff
from gendiff.cli import parse


def main():
    args = parse()
    print(
        generate_diff(args.first_file, args.second_file, formater=args.format))


if __name__ == '__main__':
    main()

'''
import argparse
import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    diff = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff[key] = f'  {key}: {data1[key]}'
            else:
                diff[key] = f'- {key}: {data1[key]}\n+ {key}: {data2[key]}'
        elif key in data1:
            diff[key] = f'- {key}: {data1[key]}'
        else:
            diff[key] = f'+ {key}: {data2[key]}'

    return '{\n' + '\n'.join(diff.values()) + '\n}'


def main():
    parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='Path to the first configuration file')
    parser.add_argument('second_file', help='Path to the second configuration file')
    parser.add_argument('-f', '--format', choices=['plain', 'json'], default='plain',
                        help='Set the format of the output. Choose from "plain" or "json". Default is "plain"')
    args = parser.parse_args()

    if hasattr(args, 'format') and args.format:
        diff = generate_diff(args.first_file, args.second_file)

        if args.format == 'json':
            print(json.dumps(json.loads(diff), indent=2))
        else:
            print(diff)
    else:
        parser.print_help()



if __name__ == '__main__':
    main()
'''