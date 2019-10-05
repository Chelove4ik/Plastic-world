import pandas as pd
from openpyxl import load_workbook


def writer(addr_input_file: str, data: pd.core.frame.DataFrame, ) -> None:
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

    addr_input_file = '\\'.join(addr_input_file.replace('/', ' ').replace('//', ' ').replace('\\', ' ').split()[:-1])

    writ = pd.ExcelWriter(f'{addr_input_file}Расписание за {months[data.columns[10].month]}.xlsx', engine='openpyxl')
    writ.book = book
    writ.sheets = dict((ws.title, ws) for ws in book.worksheets)

    data = data.iloc[:, 1:]
    data.to_excel(writ, "График", startrow=6, header=False)
    writ.save()
