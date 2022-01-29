#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("activeworkbook")
activesheet_name = excel.read_activesheet_name()
[x1, y1, x2, y2] = excel.read_range_select()

#왼쪽끝과 오른쪽 끝의 공백을 삭제하는 것
for x in range(x1, x2+1):
	for y in range(y1, y2+1):
		current_data = excel.read_cell_value(activesheet_name,[x, y])
		changed_data = str(current_data).lstrip()
		if current_data == changed_data or current_data == None or type(current_data)==type(123):
			pass
		else:
			excel.write_cell_value(activesheet_name, [x, y], changed_data)
			excel.set_cell_color(activesheet_name, [x, y], 16)
