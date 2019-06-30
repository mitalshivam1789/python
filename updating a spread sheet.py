import openpyxl
wb=openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
PU = {'Garlic':3.07,
      'Celery': 1.19,
      'Lemon':1.27}

condition = "y"
while condition == "y":
    produce = input("item whose price is increased")
    for keys,values in PU.items():
        if keys == produce:
            changed_value = input("what is the changed value")
            PU[keys]= changed_value

    condition = input("did you what to change something else")

print(PU)