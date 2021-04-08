from trees import DecisionTree

def main():
    data_path = 'gielda.txt'
    decision_tree = DecisionTree(data_path, separator=',')
    decision_tree.create_decision_table()


if __name__ == '__main__':
    main()
