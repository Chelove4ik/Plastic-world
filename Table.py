class Table:
    def __init__(self, *args):
        self.employees = list(args)

    def mutate(self):  # TODO: исправить и доделать
        for i in self.employees:
            i.mutate()

    def get_table(self):  # TODO: доделать
        pass

    def count_penalty(self):  # TODO: доделать
        pass
