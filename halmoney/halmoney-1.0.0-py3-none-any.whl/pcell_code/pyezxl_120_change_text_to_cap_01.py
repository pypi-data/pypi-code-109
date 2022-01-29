#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("activeworkbook")
activesheet_name = excel.read_activesheet_name()
[x1, y1, x2, y2] = excel.read_range_select()

for x in range(x1, x2+1):
	for y in range(y1, y2+1):
		current_data = str(excel.read_cell_value(activesheet_name,[x, y]))
		if current_data == "None" : current_data = ""

		excel.write_cell_value(activesheet_name,[x, y],current_data.upper())
