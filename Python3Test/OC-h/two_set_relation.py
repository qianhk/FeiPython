#!/usr/bin/env python
# coding=utf-8


import argparse
import os


def read_from_file(filepath):
    words_set = set(line.strip() for line in open(filepath))
    # print(f'{words_set}')
    return words_set


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='two set from file')
    parser.add_argument(
        '-f1', '--file1',
        type=str,
        default='',
        required=True,
    )
    parser.add_argument(
        '-f2', '--file2',
        type=str,
        default='',
        required=True,
    )

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args, unparsed = parser.parse_known_args()
    # print(f'sys.argv={sys.argv}\nargs={args}\nunparsed={unparsed}\nargs.pbxproj={args.pbxproj}\nargs.replacedir={args.replacedir}')
    # print(f'pbxproj={args.pbxproj}')

    file1 = os.path.abspath(args.file1)
    file2 = os.path.abspath(args.file2)
    fileExist1 = os.path.isfile(file1)
    fileExist2 = os.path.isfile(file2)
    if fileExist1 and file2:
        # x = {'spam', 'abc', 'm'}
        # y = {'h', 'abc', 'm'}
        # print(f'{x & y}')
        set1 = read_from_file(file1)
        set2 = read_from_file(file2)
        result_set = set1 & set2
        for file_h in result_set:
            print(f'{file_h}')
        # print(f'set&set{set1 & set2}')
    else:
        print(f'File  not exists or is directory')
