from pandas import DataFrame
from constants import *

class Table:
    def __init__(self, table):
        self.table: DataFrame = table

    def mutate(self):  # TODO: исправить и доделать
        for i in self.employees:
            i.mutate()

    def check(self):  # TODO: доделать
        INKbud = {'1и', '2и', '3и', '4и', '5и', '6и', '7и', '8и', '9и', '11и',
                  '12и', '22и', '24и', '26и', '28и', '56и', '57и'}
        INKsat = {'13и', '14и', '15и', '16и', '22и', '24и', '26и', '28и', '56и', '57и'}
        INKsun = {'18и', '19и', '20и', '21и', '24и', '26и', '28и', '29и', '55и', '56и', '57и'}
        VODbud = {'1в', '2в', '3в', '4в', '5в', '6в', '7в', '8в', '9в', '11в',
                  '12в', '22в', '24в', '26в', '28в', '56в', '57в'}
        VODsat = {'13в', '14в', '15в', '16в', '22в', '24в', '26в', '28в', '56в', '57в'}
        VODsun = {'18в', '19в', '20в', '21в', '24в', '26в', '28в', '29в', '55в', '56в', '57в'}
        for i in range(7, self.table.shape[0]):  # проверка ИНК смены
            for j in range(3, self.table.shape[1]):
                if self.table.columns[j].weekday() in {0, 1, 2, 3, 4}\
                        and not ((self.table[i, 2] == 'инк' and self.table[i, j] in INKbud)
                                 or (self.table[i, 2] == 'вод' and self.table[i, j] in VODbud)):
                    return False
                elif self.table.columns[j].weekday() == 5 \
                        and not ((self.table[i, 2] == 'инк' and self.table[i, j] in INKsat)
                                 or (self.table[i, 2] == 'вод' and self.table[i, j] in VODsat)):
                    return False
                elif self.table.columns[j].weekday() == 6 \
                        and not ((self.table[i, 2] == 'инк' and self.table[i, j] in INKsun)
                                 or (self.table[i, 2] == 'вод' and self.table[i, j] in VODsun)):
                    return False
                elif self.table[i, 1] == 'Водитель 2' and\
                        not (self.table.columns[j].weekday()
                             in {0, 1, 2, 3, 4} and self.table[i, j] == '25в'):
                    return False
                elif self.table[i, 1] == 'Водитель 20':
                    if self.table.columns[j].weekday() in {0, 1, 2, 3, 4} \
                            and not (self.table[i, 2] == 'вод' and self.table[i, j] in VODbud):
                        return False
                    elif self.table.columns[j].weekday() == 5 \
                            and not (self.table[i, 2] == 'вод' and self.table[i, j] in VODsat):
                        return False
                    elif self.table.columns[j].weekday() == 6 \
                            and not (self.table[i, 2] == 'вод' and self.table[i, j] in VODsun):
                        return False
        #  if TODO: ой я устал сделайте сами пункт 6 и дальше

    def crossover(self, other):
        from random import randint
        rand_index = randint(1, self.table.shape[0] - 1)
        for i in range(1, rand_index):
            for name in self.table:
                self.table.loc[i, name], other.loc[i, name] = other.table.loc[i, name], self.table.loc[i, name]

    def mutation(self):
        from random import randint
        rand_index = randint()
        for name in self.table:
            for elm in self.table[name]:
                if not name:
                    tp = elm
                    # TODO: сделать проверку на тип смены (ИНК ИЛИ ВОД)
                if not ('ФИО' in name or '№' in name or not name):
                    # if tp == tp_shift
                    from random import choice
                    elm = choice(shifts)
