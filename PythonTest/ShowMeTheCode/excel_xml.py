#!/usr/bin/env python
# coding=utf-8

import xlrd
# from lxml import etree
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
    data = {}
    rows = sheet.nrows
    cols = sheet.ncols
    kv = []
    for i in range(rows):
        for j in range(1, cols):
            if type(sheet.cell_value(i, j)) is float:
                kv.append(int(sheet.cell_value(i, j)))
            else:
                kv.append(sheet.cell_value(i, j))
        data[str(int(sheet.cell_value(i, 0)))] = kv
    return json.dumps(data, ensure_ascii=False)


# def to_xml(data):
#     # Create a document and elements
#     root = etree.Element('root')
#     stu = etree.SubElement(root, 'student')
#     # Create a comment
#     stu.append(etree.Comment(u' 学生信息表\n\t"id" : [名字, 数学, 语文, 英文]'))
#
#     # Create text
#     stu.text = data
#
#     # Save to file
#     tree = etree.ElementTree(root)
#     tree.write('student.xml', encoding='utf-8', pretty_print=True, \
#                xml_declaration=True)


if __name__ == '__main__':
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    data = read_xls('../cache/student.xls')
    # to_xml(data)
