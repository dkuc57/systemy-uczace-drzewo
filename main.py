import math


class DecisionTree:

    def __init__(self, data_path, separator):
        self.data_path = data_path
        self.separator = separator
        self.decision_table = []
        self.n_unique_values = []
        self.frequencies = None
        self.y_values = []

    def create_decision_table(self):
        file = open(self.data_path, 'r')

        while True:
            row = file.readline().strip()
            if not row:
                break
            row = [value for value in row.split(self.separator)]

            if not self.frequencies:
                self.frequencies = [{} for _ in range(len(row))]

            for index, value in enumerate(row):
                if value not in self.frequencies[index]:
                    self.frequencies[index][value] = 1
                else:
                    self.frequencies[index][value] += 1

            self.decision_table.append(row)

        self.n_unique_values = [len(values) for values in self.frequencies]
        self.y_values = [row[-1] for row in self.decision_table]

        print('Decision table was created: {}'.format(self.decision_table))


def main():
    data_path = 'gielda.txt'
    decision_tree = DecisionTree(data_path, separator=',')
    decision_tree.create_decision_table()


if __name__ == '__main__':
    main()
