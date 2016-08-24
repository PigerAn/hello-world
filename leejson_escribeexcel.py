import os
import json
import xlwt


fileJson = 'Schedules.json'

if os.path.exists(fileJson): # try path as-is
    tempfilename = fileJson

with open(tempfilename) as data_file:
    data = json.load(data_file)
    print "se leyo el archivo"


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet',cell_overwrite_ok=True)


for xx in range(len(data)):
    # print data[xx]['SERVICECATEGORY']
    # print data[xx]['SERVICENAME']

    ws.write(xx, 0, data[xx]['SERVICECATEGORY'])
    ws.write(xx, 1,data[xx]['SERVICENAME'])
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 4)
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))
wb.save('ClassSchedulesCategories.xls')