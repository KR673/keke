import openpyxl
from tools.data_operate import db_exec


def get_excel_data(file_name):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb['Sheet1']

    data = [] 
    for index,row in enumerate(sheet.rows):
        if index == 0:
            continue
        data.append('-'.join([(str(cell.value) if str(cell.value) != '' else '/') for index, cell in enumerate(row) if index <= 3]).split('-'))
    return data

if __name__ == "__main__":
    data = []
    data_low = get_excel_data('./source/people_low.xlsx')
    data_lot = get_excel_data('./source/people_lot.xlsx')

    data.extend(data_low)
    data.extend(data_lot)
    sql = ""
    for d in data:
        if len(d) < 6:
            print(d)
            continue
        sql += "INSERT INTO enroll (city, department, positon_code, position, enroll_num, apply_num) values ('{}', '{}', '{}', '{}', '{}', '{}');".format(d[0], d[1], d[2], d[3], d[4], d[5])
    db_exec('Delete from enroll')
    db_exec(sql)