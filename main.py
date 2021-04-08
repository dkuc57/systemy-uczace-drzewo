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

    @staticmethod
    def calculate_entropy(values):
        return - sum([value * math.log(value, 2) if value != 0 else 0 for value in values])

    def calculate_info_for_selected_column(self, column_index):
        info_value = 0
        column_values = [row[column_index] for row in self.decision_table]
        frequencies_in_col = self.frequencies[column_index]

        for this_value, frequency in frequencies_in_col.items():
            selected_y = [self.y_values[index] for index, value in enumerate(column_values) if value == this_value]
            power_of_this_value = frequency / len(column_values)
            partial_entropy = self.calculate_entropy([selected_y.count(v) / len(selected_y) for v in set(selected_y)])
            info_value += (power_of_this_value * partial_entropy)

        return info_value

    def calculate_gain_for_selected_column(self, column_index):
        y_entropy_value = self.calculate_entropy([self.y_values.count(y) / len(self.y_values) for y in
                                                  set(self.y_values)])
        info_value = self.calculate_info_for_selected_column(column_index)
        return y_entropy_value - info_value


def main():
    data_path = 'gielda.txt'
    decision_tree = DecisionTree(data_path, separator=',')
    decision_tree.create_decision_table()
    info_a1 = decision_tree.calculate_info_for_selected_column(0)
    gain_a2 = decision_tree.calculate_gain_for_selected_column(1)
    print('Info a1 = {} \nGain a2 = {}'.format(info_a1, gain_a2))

if __name__ == '__main__':
    main()
