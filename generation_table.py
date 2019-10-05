from random import choice
from pandas import DataFrame


def generation_table(start_table, employee, days, driver, collector, first_week_day):
    table = []
    first_week_day = first_week_day
    INKbud = ['1и', '2и', '3и', '4и', '5и', '6и', '7и', '8и', '9и', '11и',
              '12и', '22и', '24и', '26и', '28и', '56и', '57и', 'В']
    INKsat = ['13и', '14и', '15и', '16и', '22и', '24и', '26и', '28и', '56и', '57и', 'В']
    INKsun = ['18и', '19и', '20и', '21и', '24и', '26и', '28и', '29и', '55и', '56и', '57и', 'В']
    VODbud = ['1в', '2в', '3в', '4в', '5в', '6в', '7в', '8в', '9в', '11в',
              '12в', '22в', '24в', '26в', '28в', '56в', '57в', 'В']
    VODsat = ['13в', '14в', '15в', '16в', '22в', '24в', '26в', '28в', '56в', '57в', 'В']
    VODsun = ['18в', '19в', '20в', '21в', '24в', '26в', '28в', '29в', '55в', '56в', '57в', 'В']
    for i in range(int(employee)):
        employee_grafic = []
        if employee + 1 <= collector:
            Driver = False
            Collector = True
        else:
            Collector = False
            Driver = True
        k = 0
        for j in range(7, 3, -1):
            if start_table.iloc[i, j] != "О" and start_table.iloc[i, j] != "В":
                k += 1
            else:
                break
        for j in range(days):
            if start_table.iloc[0 + i, 8 + j] == "О":
                shift = "О"
            elif k == 5 and start_table.iloc[0 + i, 8 + j] != "О":
                shift = "В"
                k = 0
            elif i + 1 == driver and Driver and 0 <= (first_week_day + days) % 6 <= 4:
                shift = choice(['25в', '25в', '25в', 'В'])
            elif 0 <= (first_week_day + days) % 6 <= 4:
                if Driver:
                    shift = choice(VODbud)
                if Collector:
                    if employee_grafic[j - 1] == "3и":
                        shift = choice(['3и', '3и', '3и', 'В'])
                    else:
                        shift = choice(INKbud)
            elif (first_week_day + days) % 6 == 5:
                if Driver:
                    shift = choice(VODsat)
                if Collector:
                    if employee_grafic[j - 1] == "3и":
                        shift = choice(['3и', '3и', '3и', 'В'])
                    else:
                        shift = choice(INKsat)
            elif (first_week_day + days) % 6 == 6:
                if Driver:
                    shift = choice(VODsun)
                if Collector:
                    if employee_grafic[j - 1] == "3и":
                        shift = choice(['3и', '3и', '3и', 'В'])
                    else:
                        shift = choice(INKsun)
            if shift != "В":
                k += 1
            if shift == "О":
                k = 0
            employee_grafic.append(shift)
        table.append(employee_grafic)
    table = DataFrame(data=table)
    print('table')
    return table
