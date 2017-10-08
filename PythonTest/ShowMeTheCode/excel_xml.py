#!/usr/bin/env python
# coding=utf-8

import xlrd
from lxml import etree
import json
import io
import sys


def read_xls(fromfile):
    # with open(fromfile) as f:
    #     content = f.read()
    #
    # print (content)
    # return

    book = xlrd.open_workbook(fromfile)
    sheet = book.sheet_by_name('student')
    dataList = []
    rows = sheet.nrows
    cols = sheet.ncols

    for row in range(rows):
        dict = {}
        dict['stu_no'] = sheet.cell_value(row, 0)
        dict['stu_name'] = sheet.cell_value(row, 1)
        dict['chinese'] = int(sheet.cell_value(row, 2))
        dict['math'] = int(sheet.cell_value(row, 3))
        dict['english'] = int(sheet.cell_value(row, 4))
        dataList.append(dict)
    return (dataList, json.dumps(dataList, ensure_ascii=False))


def to_json_file(json):
    with open('../cache/student_new.json', 'wt') as f:
        f.write(json)


def to_xml(dataList):
    root = etree.Element('root')
    # Create a comment
    root.append(etree.Comment(u' 学生信息表\n\t[学号, 姓名, 语文, 数学, 英语]'))
    stuList = etree.SubElement(root, 'student_list')

    # Create student item
    for item in dataList:
        stu = etree.SubElement(stuList, 'stu')
        stu.set('stu_no', item['stu_no'])
        stu.text = item['stu_name']
        stu.set('chinese', str(item['chinese']))
        stu.set('math', str(item['math']))
        stu.set('english', str(item['english']))


    # Save to file
    tree = etree.ElementTree(root)
    tree.write('../cache/student_list.xml', encoding='utf-8', pretty_print=True, \
               xml_declaration=True)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    (dataList, json) = read_xls('../cache/student.xls')
    to_json_file(json)
    to_xml(dataList)
