from openpyxl import load_workbook
from Table import Table
import pandas as pd
from my_parser import parser
from generation_table import generation_table

def writer(addr_input_file: str, data: pd.core.frame.DataFrame, addr_for_save=None) -> None:
    months = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь',
    }
    book = load_workbook(addr_input_file)

    if addr_for_save is None:
        addr_for_save = '/'.join(
            addr_input_file.replace('/', '*').replace('//', '*').replace('\\', '*').split('*')[:-1])
    else:
        addr_for_save = '/'.join(addr_for_save.replace('/', '*').replace('//', '*').replace('\\', '*').split('*')[:-1])
    print(data.columns[10])
    print(months[data.columns[10]])
    writ = pd.ExcelWriter(f'{addr_for_save}Расписание.xlsx', engine='openpyxl')
    print(f'{addr_for_save}Расписание за {months[data.columns[10]]}.xlsx')
    writ.book = book
    writ.sheets = dict((ws.title, ws) for ws in book.worksheets)

    data = data.iloc[:, 1:]
    data.to_excel(writ, "График", startrow=6, header=False, startcol=8, index=False)
    writ.save()


# table = parser('data/input_data.xlsx')
# tables = [Table(generation_table(table, table.shape[0], 30, 31, 25, table.columns[8].weekday())) for i in range(1000)]

# table = parser('C:/Users/User/Downloads/Хакатон IT График СЕНТЯБРЬ(задание   список правил).xlsx')
# writer('data/input_data.xlsx', tables[0].get_table())
