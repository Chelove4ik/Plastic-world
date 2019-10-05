import pandas as pd


def parser(addr_file: str) -> pd.core.frame.DataFrame:  # ex: val = parser('data/input_data.xlsx')
    input_data = pd.read_excel(addr_file, sheet_name=1, header=5, )

    input_data = input_data.iloc[:, :list(input_data.columns).index('Машина')]

    y = 0
    while input_data.iloc[y][2] in ['вод', 'инк']:
        y += 1
    input_data = input_data.iloc[:y, :]

    return input_data
