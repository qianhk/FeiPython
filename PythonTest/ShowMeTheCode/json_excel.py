#!/usr/bin/env python
# coding=utf-8

import json
import xlwt

testfile = 'student.json'
savename = '../cache/student.xls'
sheetname = 'student'


def json_to_excel():
    info = get_json(testfile)
    workbook = xlwt.Workbook(encoding='utf-8')
    workbook.set_owner('KaiFromPython')
    sheet = workbook.add_sheet(sheetname)

    row_total = len(info)
    info1 = info[str(1)]
    col_total = len(info1)
    # The keys of dict is special, so we just use 1, 2, 3
    for r in range(row_total):
        sheet.write(r, 0, r + 1)
        for c in range(col_total):
            # Get values by the key
            vals = info[str(r + 1)]
            sheet.write(r, c + 1, vals[c])

    workbook.save(savename)


# Convert json format file to python object
def get_json(testfile):
    with open(testfile, 'r') as f:
        # The codec should be the same as the file encoding.
        text = f.read()
        return json.loads(text)


if __name__ == '__main__':
    json_to_excel()
