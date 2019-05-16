#!/usr/bin/env python3
# coding=utf-8

import argparse
import os
import sys
import time
import shutil
import re

MODIFY_FILE_SUFFIX = {'.h', '.m', '.mm'}

IGNORE_DIR_SUFFIX = {'.xcworkspace', '.xcodeproj', '.xcassets', '.xcdatamodeld'}
IGNORE_DIR = {'Pods', 'PodMainDependencies'}


def add_ok_file_to_list(dest_files, dir):
    # print(f'will list dir: {dir}')
    try:
        inner_dir = os.listdir(dir)
    except:
        print(f"listdir({dir}) Unexpected error: {sys.exc_info()[0]}")
    else:
        for path in inner_dir:
            path = os.path.normpath(dir + os.path.sep + path)
            base_name = os.path.basename(path)
            if base_name[0] == '.':
                continue
            suffix = os.path.splitext(path)[1]
            # print(f'base_name={base_name} suffix={suffix}')  # (xx/a.txt:a.txt:.txt xxx/Pods:Pods: xxx/.txt:.txt:
            if os.path.isfile(path):
                if suffix in MODIFY_FILE_SUFFIX:
                    # print(f'file: {path}')
                    dest_files.append(path)
            else:
                if base_name not in IGNORE_DIR and suffix not in IGNORE_DIR_SUFFIX:
                    # print(f'dir: {path}')
                    add_ok_file_to_list(dest_files, path)

    # for dir_path, subpaths, files in os.walk(dir): //不需要的路径也遍历了
    #     for file in files:
    #         path = os.path.normpath(dir_path + os.path.sep + file)
    #         print(f'{path}')


def get_replace_public_h_files(framework, dest_dirs):
    print(f'will replace public .h file, framework name: {framework}')
    dest_files = []
    for dest_dir in dest_dirs:
        dest_dir = os.path.abspath(dest_dir)
        print(f'search files in {dest_dir}')
        add_ok_file_to_list(dest_files, dest_dir)
    return dest_files


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


# def modify_file_import(path, framework, public_list):
#     print(f'modify file import: {path}')
#     # try:
#     #     with open(path, 'wt') as reader:
#     #         pass
#     # except:
#     #     print(f"modify file import '{path}': Unexpected error: {sys.exc_info()[0]}")
#     # os.system(f'cat {path}')
#     for h_name in public_list:
#         sed_cmd = """\"{h_name}\"""".format(h_name=h_name, )
#         print(sed_cmd)
#         # os.system(f'sed s/{h_name}/<{framework}>/g')


def modify_files_import2(dest_files, framework, public_list):
    sed_cmds = []
    for h_name in public_list:
        sed_cmd = """sed -i '' 's/\"{h_name}\"/<{frame}\/{h_name}>/g'""".format(h_name=h_name, frame=framework)
        # print(sed_cmd)
        sed_cmds.append(sed_cmd)
    count = 0
    for file in dest_files:
        for sed_cmd in sed_cmds:
            full_sed_cmd = '{} "{}"'.format(sed_cmd, file)
            count += 1
            print(full_sed_cmd)
            # os.system(full_sed_cmd)
    print(f'total replace {count} times')


def modify_files_import(dest_files, framework, public_list):
    sed_cmd = "sed -i ''"
    for h_name in public_list:
        sed_cmd += """ -e 's/\"{h_name}\"/<{frame}\/{h_name}>/g'""".format(h_name=h_name, frame=framework)
        # print(sed_cmd)
    count = 0
    for file in dest_files:
        full_sed_cmd = '{} "{}"'.format(sed_cmd, file)
        count += 1
        # print(full_sed_cmd)
        os.system(full_sed_cmd)
    print(f'total replace {count} times')


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

    pbxproj = os.path.abspath(args.pbxproj)
    exist = os.path.isfile(pbxproj)
    if exist:
        # print(f'File "{pbxproj}" exists.')
        if os.access(pbxproj, os.R_OK):
            public_list = parse_pubic_h_file(pbxproj)
            if len(public_list) > 0:
                # public_list = public_list[:1]  # for test
                print(f'found {len(public_list)} public .h file in {pbxproj}')
                dest_files = get_replace_public_h_files(args.framework, args.replacedir)
                if len(dest_files) > 0:
                    print(f'found {len(dest_files)} files need to be replace')
                    # print(f'found {len(dest_files)} files, dest_files: {dest_files}')
                    # dest_files = ['/the/path/to/file.m', '/the/path/to/file.h']
                    # dest_files = dest_files[:5]  # for test
                    modify_files_import(dest_files, args.framework, public_list)
                    print(f'Done.')
                else:
                    print(f'not found dest files to be replace.')
            else:
                print(f'public .h config not found.')
        else:
            print(f'File "{pbxproj}" is not accessible to read')
    else:
        print(f'File "{pbxproj}" not exists or is directory')
