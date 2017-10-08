#!/usr/bin/env python
# coding=utf-8

import json
import xlwt
import sys

testfile = 'student.json'
savename = '../cache/student.xls'
sheetname = 'student'


def json_to_excel():
    studentList = get_json(testfile)
    # workbook = xlwt.Workbook()
    workbook = xlwt.Workbook(encoding='utf-8') #实际试了编码参数有无utf8,生成的文件md5一样
    workbook.set_owner('KaiFromPython')
    sheet = workbook.add_sheet(sheetname)

    index = 0
    for stu in studentList:
        str_no = str(stu['stu_no'])
        sheet.write(index, 0, str_no)
        str_stu_name = str(stu['stu_name'])
        sheet.write(index, 1, str_stu_name)
        sheet.write(index, 2, str(stu['chinese']))
        sheet.write(index, 3, str(stu['math']))
        sheet.write(index, 4, str(stu['english']))
        index += 1

    workbook.save(savename)


# Convert json format file to python object
def get_json(testfile):
    with open(testfile, 'r') as f:
        # The codec should be the same as the file encoding.
        text = f.read()
        return json.loads(text)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    json_to_excel()

