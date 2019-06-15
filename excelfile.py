import xlsxwriter
import xlrd
workbook = xlsxwriter.Workbook('./first_excel_file.xlsx')
worksheet_data = workbook.add_worksheet('data')
worksheet_analysis = workbook.add_worksheet('analysis')
print(workbook.sheetnames)
print(workbook.sheetnames['analysis'])
worksheet_analysis.write("A1","spock")
worksheet_analysis.write(1,0,"kirk")
worksheet_analysis.write(3,4,"kirk")
#worksheet_analysis.set_column("E:E",30)
workbook.close()
file_location = "first_excel_file.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)
print(sheet)
data=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]
print(data)
print()