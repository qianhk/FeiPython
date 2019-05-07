#!/usr/bin/env python3
# coding=utf-8

import argparse
import os
import sys
import time
import shutil
import re


def parse_pubic_h_file(pbxproj):
    with open(pbxproj, 'rt') as reader:
        line = reader.readline()
        header_section = False
        build_section = False
        header_strings = ''
        build_strings = ''
        while line != '':
            if line == '/* Begin PBXHeadersBuildPhase section */\n':
                header_section = True

            if header_section:
                # print(line, end='')
                header_strings += line

            if line == '/* End PBXHeadersBuildPhase section */\n':
                header_section = False

            if line == '/* Begin PBXBuildFile section */\n':
                build_section = True

            if build_section:
                # print(line, end='')
                build_strings += line

            if line == '/* End PBXBuildFile section */\n':
                build_section = False

            line = reader.readline()

            # print(f'header strings:\n{header_strings}')
            # print(f'build strings:\n{build_strings}')

        pattern = re.compile('(\w+) /\* (.+) in Headers')
        result = pattern.findall(header_strings)

        public_list = []
        for group in result:
            if re.search(group[0] + '.+Public,', build_strings):
                # print(f'code={group[0]} name={group[1]}')
                public_list.append(group[1])

        # print(f'public .h, size={len(public_list)} list={public_list}')
        return public_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='extract public .h file in project.pbxproj')
    parser.add_argument(
        '-p', '--pbxproj',
        type=str,
        default='',
        metavar='pbxproj',
        # dest='simple_value',
        required=True,
        help='project.pbxproj file path'
    )

    parser.add_argument(
        '-f', '--framework',
        type=str,
        default='',
        # metavar='pbxproj',
        # dest='simple_value',
        required=True,
        help='framework name, example: UIKit'
    )

    parser.add_argument(
        '-d', '--replacedir',
        type=str,
        default=[],
        nargs='+',
        # action='append',
        metavar='dir',
        required=True,
        help='.h .m .mm be replaced in these dir'
    )

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args, unparsed = parser.parse_known_args()
    # print(f'sys.argv={sys.argv}\nargs={args}\nunparsed={unparsed}\nargs.pbxproj={args.pbxproj}\nargs.replacedir={args.replacedir}')
    print(f'pbxproj={args.pbxproj} framwork={args.framework} replacedir={args.replacedir}')

    exist = os.path.isfile(args.pbxproj)
    if exist:
        # print(f'File "{args.pbxproj}" exists.')
        if os.access(args.pbxproj, os.R_OK):
            public_list = parse_pubic_h_file(args.pbxproj)
            if len(public_list) > 0:
                print(f'found {len(public_list)} public .h file')
            else:
                print(f'public .h config not found.')
        else:
            print(f'File "{args.pbxproj}" is not accessible to read')
    else:
        print(f'File "{args.pbxproj}" not exists or is directory')
