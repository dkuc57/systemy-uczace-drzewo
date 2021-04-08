from trees import DecisionTree

def main():
    data_path = 'gielda.txt'
    decision_tree = DecisionTree(data_path, separator=',')
    decision_tree.create_decision_table()
    info_a1 = decision_tree.calculate_info_for_selected_column(0)
    gain_a2 = decision_tree.calculate_gain_for_selected_column(1)
    print('Info a1 = {} \nGain a2 = {}'.format(info_a1, gain_a2))

if __name__ == '__main__':
    main()
