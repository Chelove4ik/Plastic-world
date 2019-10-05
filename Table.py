class Table:
    def __init__(self, table):
        self.table = table

    def check(self):
        from constants import INKbud, INKsat, INKsun, VODbud, VODsat, VODsun, hour8, hour9, hour10
        penalty = 0
        for i in range(1, self.table.shape[0]):  # проверка ИНК смены
            for j in range(8, self.table.shape[1]):
                if self.table.columns[j].weekday() in {0, 1, 2, 3, 4}\
                        and not ((self.table[i, 2] == 'инк' and self.table[i, j] in INKbud)
                                 or (self.table[i, 2] == 'вод' and self.table[i, j] in VODbud)):
                    penalty += 100
                elif self.table.columns[j].weekday() == 5 \
                        and not ((self.table[i, 2] == 'инк' and self.table[i, j] in INKsat)
                                 or (self.table[i, 2] == 'вод' and self.table[i, j] in VODsat)):
                    penalty += 100
                elif self.table.columns[j].weekday() == 6 \
                        and not ((self.table[i, 2] == 'инк' and self.table[i, j] in INKsun)
                                 or (self.table[i, 2] == 'вод' and self.table[i, j] in VODsun)):
                    penalty += 100
                elif self.table[i, 1] == 'Водитель 2' and\
                        not (self.table.columns[j].weekday()
                             in {0, 1, 2, 3, 4} and self.table[i, j] == '25в'):
                    penalty += 100
                elif self.table[i, 1] == 'Водитель 20':
                    if self.table.columns[j].weekday() in {0, 1, 2, 3, 4} \
                            and not (self.table[i, 2] == 'вод' and self.table[i, j] in VODbud):
                        penalty += 100
                    elif self.table.columns[j].weekday() == 5 \
                            and not (self.table[i, 2] == 'вод' and self.table[i, j] in VODsat):
                        penalty += 100
                    elif self.table.columns[j].weekday() == 6 \
                            and not (self.table[i, 2] == 'вод' and self.table[i, j] in VODsun):
                        penalty += 100
                elif self.table.columns[j].weekday() in {0, 1, 2, 3, 4} and not all(k in ['1и', '2и', '3и', '4и', '5и', '6и', '7и', '8и', '9и', '11и', '12и',
                                 '22и', '24и', '26и', '28и', '56и', '57и', '1в', '2в', '3в', '4в',
                                 '5в', '6в', '7в', '8в', '9в', '11в', '12в', '22в', '24в', '25в',
                                 '26в', '28в', '56в', '57в'] for k in self.table.iloc[:, j]):
                    penalty += 100
                elif self.table.columns[j].weekday() == 5 and not all(
                        k in ['13и', '14и', '15и', '16и', '22и', '24и', '26и', '28и', '56и',
                              '57и', '13в', '14в', '15в', '16в', '22в', '24в', '26в', '28в',
                              '56в', '57в'] for k in self.table.iloc[:, j]):
                    penalty += 100
                elif self.table.columns[j].weekday() == 6 and not all(
                        k in ['18и', '19и', '20и', '21и', '24и', '26и', '28и', '29и', '55и',
                              '56и', '57и', '18в', '19в', '20в', '21в', '24в', '26в', '28в',
                              '29в', '55в', '56в', '57в'] for k in self.table.iloc[:, j]):
                    penalty += 100  # пункт 9 проверяется при генерации таблиц и не изменяется далее
                elif all(k != 'О' or k != 'В' for k in self.table.loc[i, j - 4:j]):
                    penalty += 100
                elif self.table.loc[i, j] in {'1и', '2и', '3и', '4и', '5и', '6и', '9и', '22и',
                                              '24и', '26и', '28и', '1в', '2в', '3в', '4в', '5в',
                                              '6в', '9в', '22в', '24в', '25в', '26в', '28в',
                                              '14и', '22и', '24и', '26и', '28и', '14в', '22в',
                                              '24в', '26в', '28в', '18и', '24и', '26и', '28и',
                                              '29и', '55и', '18в', '24в', '26в', '28в', '29в',
                                              '55в'} \
                        and (self.table.loc[i, j - 1] in {'7и', '8и', '11и', '7в', '8в', '11в',
                                                          '25в', '13и', '15и', '16и', '13в', '15в',
                                                          '16в', '19и', '20и', '21и', '19в', '20в',
                                                          '21в'}
                             or self.table.loc[i, j - 1] in {'12и', '56и', '57и', '12в', '56в', '57в', '56и',
                                                             '57и', '56в', '57в', '56и', '57и', '56в', '57в'}):
                    penalty += 100
                elif self.table.loc[i, j - 1] == '3и' and not (self.table.loc[i, j] == 'В' or
                                                               self.table.loc[i, j] == 'О' or
                                                               self.table.loc[i, j] == '3и'):
                    penalty += 100
        return penalty

    def crossover(self, other):
        from random import randint
        rand_index = randint(1, self.table.shape[0] - 1)
        for i in range(1, rand_index):
            for name in self.table:
                self.table.loc[i, name], other.loc[i, name] = other.table.loc[i, name], self.table.loc[i, name]

    def mutation(self):
        from constants import shifts
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

    def get_table(self):
        return self.table
