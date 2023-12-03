import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def find_full_number_by_index(data, number_index):
    start_index = -1
    end_index = -1
    number_str = ""
    iterator = number_index['column']
    while iterator >= 0:
        if data[number_index['row']][iterator].isdigit():
            start_index = iterator
            iterator -= 1
        else:
            break
    iterator = number_index['column']
    while iterator < (len(data[0]) - 1):
        if data[number_index['row']][iterator].isdigit():
            end_index = iterator
            iterator += 1
        else:
            break
    for char in data[number_index['row']][start_index:end_index+1]:
        number_str += char
    return int(number_str)

def find_numbers_two_lists(data, list_of_indexes:list):
    first_number = find_full_number_by_index(data, list_of_indexes[0][0])
    second_number = find_full_number_by_index(data, list_of_indexes[1][0])
    return first_number, second_number

def find_numbers_one_list(data, list_of_indexes:list):
    first_number = find_full_number_by_index(data, list_of_indexes[0][0])
    second_number = find_full_number_by_index(data, list_of_indexes[0][1])
    return first_number, second_number

def check_indexes_for_same_number(list_of_indexes:list):
    if len(list_of_indexes) == 1:
        return list_of_indexes
    elif len(list_of_indexes) == 2:
        if (list_of_indexes[1]['column'] - list_of_indexes[0]['column']) == 1:
            list_of_indexes.pop()
    elif len(list_of_indexes) == 3:
        if (list_of_indexes[1]['column'] - list_of_indexes[0]['column']) == 1:
            if (list_of_indexes[2]['column'] - list_of_indexes[1]['column']) == 1:
                list_of_indexes.pop()
                list_of_indexes.pop()
    return list_of_indexes


def process_found_lists(dict_list_of_indexes_first:dict, dict_list_of_indexes_last:dict):
    list_of_indexes = []

    dict_list_of_indexes = {
        'r1': dict_list_of_indexes_first['r1'],
        'r2': dict_list_of_indexes_first['r2'],
        'r3': dict_list_of_indexes_first['r3']
    }

    if len(dict_list_of_indexes_last['r1']) != 0:
        dict_list_of_indexes['r1'].append(dict_list_of_indexes_last['r1'][0])
    if len(dict_list_of_indexes_last['r2']) != 0:
        dict_list_of_indexes['r2'].append(dict_list_of_indexes_last['r2'][0])
    if len(dict_list_of_indexes_last['r3']) != 0:
        dict_list_of_indexes['r3'].append(dict_list_of_indexes_last['r3'][0])

    indexes = check_indexes_for_same_number(dict_list_of_indexes['r1'])
    if len(indexes) != 0:
        list_of_indexes.append(indexes)
    indexes = check_indexes_for_same_number(dict_list_of_indexes['r2'])
    if len(indexes) != 0:
        list_of_indexes.append(indexes)
    indexes = check_indexes_for_same_number(dict_list_of_indexes['r3'])
    if len(indexes) != 0:
        list_of_indexes.append(indexes)

    return list_of_indexes


def check_line_for_symbol(data, start_row, start_column, length):
    counter = 0
    list_of_indexes = []

    while counter < length:
        if data[start_row][start_column + counter].isdigit():
            list_of_indexes.append({'row': start_row, 'column': (start_column + counter)})
        counter += 1
    return list_of_indexes

def check_adjacent_first_digit(data, start_index, row_counter, column_limit, row_limit):
    list_of_indexes1 = []
    list_of_indexes2 = []
    list_of_indexes3 = []

    if (start_index - 1) >= 0 and start_index < column_limit:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            list_of_indexes1 = check_line_for_symbol(data, row_counter-1, start_index-1, 2)
            list_of_indexes2 = check_line_for_symbol(data, row_counter, start_index-1, 1)
            list_of_indexes3 = check_line_for_symbol(data, row_counter+1, start_index-1, 2)
        elif row_counter == 0:
            list_of_indexes2 = check_line_for_symbol(data, row_counter, start_index-1, 1)
            list_of_indexes3 = check_line_for_symbol(data, row_counter+1, start_index-1, 2)
        else: # row counter on the bottom
            list_of_indexes1 = check_line_for_symbol(data, row_counter-1, start_index-1, 2)
            list_of_indexes2 = check_line_for_symbol(data, row_counter, start_index-1, 1)
    elif start_index == 0:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            list_of_indexes1 = check_line_for_symbol(data, row_counter-1, start_index, 1)
            list_of_indexes2 = check_line_for_symbol(data, row_counter+1, start_index, 1)
        elif row_counter == 0:
            list_of_indexes1 = check_line_for_symbol(data, row_counter+1, start_index, 1)
        else: # row counter on the bottom
            list_of_indexes1 = check_line_for_symbol(data, row_counter-1, start_index, 1)

    dict_list_of_indexes = {
        'r1': list_of_indexes1,
        'r2': list_of_indexes2,
        'r3': list_of_indexes3
    }
    return dict_list_of_indexes

def check_adjacent_last_digit(data, start_index, row_counter, column_limit, row_limit):
    list_of_indexes1 = []
    list_of_indexes2 = []
    list_of_indexes3 = []

    if start_index >= 0 and (start_index + 1) < column_limit:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            list_of_indexes1 = check_line_for_symbol(data, row_counter-1, start_index+1, 1)
            list_of_indexes2 = check_line_for_symbol(data, row_counter, start_index+1, 1)
            list_of_indexes3 = check_line_for_symbol(data, row_counter+1, start_index+1, 1)
        elif row_counter == 0:
            list_of_indexes2 = check_line_for_symbol(data, row_counter, start_index+1, 1)
            list_of_indexes3 = check_line_for_symbol(data, row_counter+1, start_index+1, 1)
        else: # row counter on the bottom
            list_of_indexes1 = check_line_for_symbol(data, row_counter-1, start_index+1, 1)
            list_of_indexes2 = check_line_for_symbol(data, row_counter, start_index+1, 1)
    dict_list_of_indexes = {
        'r1': list_of_indexes1,
        'r2': list_of_indexes2,
        'r3': list_of_indexes3
    }
    return dict_list_of_indexes

def check_adjacent_indexes(data, asterisk_index, row_counter,
                            column_limit, row_limit):
    dict_list_of_indexes_first = {}
    dict_list_of_indexes_last = {}
    list_of_indexes = []

    dict_list_of_indexes_first = check_adjacent_first_digit(data, asterisk_index, row_counter, column_limit, row_limit)
    dict_list_of_indexes_last = check_adjacent_last_digit(data, asterisk_index, row_counter, column_limit, row_limit)

    list_of_indexes = process_found_lists(dict_list_of_indexes_first, dict_list_of_indexes_last)
    return list_of_indexes

def main():
    data = []
    result = 0
    with open('input.txt', 'r') as iFile:
        data = iFile.readlines()
    row_counter = 0
    row_limit = len(data)
    column_limit = len(data[0]) - 1

    while row_counter < len(data):
        column_iter = 0
        list_of_indexes = []
        asterisk_index = -1
        number1 = -1
        number2 = -1
        while column_iter < column_limit:
            if data[row_counter][column_iter] == '*':
                asterisk_index = column_iter
                list_of_indexes = check_adjacent_indexes(data, asterisk_index, row_counter,
                                                                    column_limit, row_limit)
                print("Length of the list: ", len(list_of_indexes))
                if len(list_of_indexes) == 2:
                    number1, number2 = find_numbers_two_lists(data, list_of_indexes)
                    result += (number1 * number2)
                elif len(list_of_indexes) == 1:
                    if len(list_of_indexes[0]) == 2:
                        number1, number2 = find_numbers_one_list(data, list_of_indexes)
                        result += (number1 * number2)
            column_iter += 1
        row_counter += 1
    print(result)

if __name__ == "__main__":
    main()