from openpyxl import long_workbook



def excel_read(file,sheet):
    workbook=long_workbook(file)
    wc=workbook['sheet']
    data=[]
    for row in wc.iter_rows(min_row=2,value_only=True):
        data.append(row)
        return data