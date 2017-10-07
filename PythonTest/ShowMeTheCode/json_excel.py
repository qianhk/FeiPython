#!/usr/bin/env python
# coding=utf-8

import json
import xlwt

testfile = 'student.json'
savename = '../cache/student.xls'
sheetname = 'student'


def json_to_excel():
    studentList = get_json(testfile)
    workbook = xlwt.Workbook(encoding='utf-8')
    workbook.set_owner('KaiFromPython')
    sheet = workbook.add_sheet(sheetname)

    index = 0
    for stu in studentList:
        sheet.write(index, 0, stu['stu_no'])
        sheet.write(index, 1, stu['stu_name'])
        sheet.write(index, 2, stu['chinese'])
        sheet.write(index, 3, stu['math'])
        sheet.write(index, 4, stu['english'])
        index += 1

    workbook.save(savename)


# Convert json format file to python object
def get_json(testfile):
    with open(testfile, 'r') as f:
        # The codec should be the same as the file encoding.
        text = f.read()
        return json.loads(text)


if __name__ == '__main__':
    json_to_excel()

