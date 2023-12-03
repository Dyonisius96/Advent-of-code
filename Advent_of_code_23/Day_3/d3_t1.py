import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_line_for_symbol(data, start_row, start_column, length):
    counter = 0
    symbol_found = False
    while counter < length:
        if data[start_row][start_column + counter] != '.':
            symbol_found = True
            break
        counter += 1
    return symbol_found

def check_adjacent_first_digit(data, start_index, row_counter, column_limit, row_limit):
    if (start_index - 1) >= 0 and start_index < column_limit:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            if check_line_for_symbol(data, row_counter-1, start_index-1, 2):
                return True
            if check_line_for_symbol(data, row_counter, start_index-1, 1):
                return True
            if check_line_for_symbol(data, row_counter+1, start_index-1, 2):
                return True
        elif row_counter == 0:
            if check_line_for_symbol(data, row_counter, start_index-1, 1):
                return True
            if check_line_for_symbol(data, row_counter+1, start_index-1, 2):
                return True
        else: # row counter on the bottom
            if check_line_for_symbol(data, row_counter-1, start_index-1, 2):
                return True
            if check_line_for_symbol(data, row_counter, start_index-1, 1):
                return True
    elif start_index == 0:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            if check_line_for_symbol(data, row_counter-1, start_index, 1):
                return True
            if check_line_for_symbol(data, row_counter+1, start_index, 1):
                return True
        elif row_counter == 0:
            if check_line_for_symbol(data, row_counter+1, start_index, 1):
                return True
        else: # row counter on the bottom
            if check_line_for_symbol(data, row_counter-1, start_index, 1):
                return True

def check_adjacent_last_digit(data, start_index, row_counter, column_limit, row_limit):
    if start_index >= 0 and (start_index + 1) < column_limit:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            if check_line_for_symbol(data, row_counter-1, start_index, 2):
                return True
            if check_line_for_symbol(data, row_counter, start_index+1, 1):
                return True
            if check_line_for_symbol(data, row_counter+1, start_index, 2):
                return True
        elif row_counter == 0:
            if check_line_for_symbol(data, row_counter, start_index+1, 1):
                return True
            if check_line_for_symbol(data, row_counter+1, start_index, 2):
                return True
        else: # row counter on the bottom
            if check_line_for_symbol(data, row_counter-1, start_index, 2):
                return True
            if check_line_for_symbol(data, row_counter, start_index+1, 1):
                return True
    elif start_index + 1 == column_limit:
        if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
            # do normal check all around
            if check_line_for_symbol(data, row_counter-1, start_index, 1):
                return True
            if check_line_for_symbol(data, row_counter+1, start_index, 1):
                return True
        elif row_counter == 0:
            if check_line_for_symbol(data, row_counter+1, start_index, 1):
                return True
        else: # row counter on the bottom
            if check_line_for_symbol(data, row_counter-1, start_index, 1):
                return True

def check_adjacent_middle_digit(data, start_index, row_counter, column_limit, row_limit):
    if (row_counter - 1) >= 0 and (row_counter + 1) < row_limit:
        # do normal check all around
        if check_line_for_symbol(data, row_counter-1, start_index, 1):
            return True
        if check_line_for_symbol(data, row_counter+1, start_index, 1):
            return True
    elif row_counter == 0:
        if check_line_for_symbol(data, row_counter+1, start_index, 1):
            return True
    else: # row counter on the bottom
        if check_line_for_symbol(data, row_counter-1, start_index, 1):
            return True

def check_adjacent_indexes(data, start_index,
                            end_index, row_counter,
                            column_limit, row_limit):
    symbol_found = False
    if start_index == end_index:
        # if we have 1 digit, do first and last digit check on the same number to check all adjacent places
        symbol_found = check_adjacent_first_digit(data, start_index, row_counter, column_limit, row_limit)
        if symbol_found != True:
            symbol_found = check_adjacent_last_digit(data, start_index, row_counter, column_limit, row_limit)
    else:
        column_iter = start_index
        while column_iter <= end_index:
            if column_iter == start_index:
                symbol_found = check_adjacent_first_digit(data, column_iter, row_counter, column_limit, row_limit)
            elif column_iter == end_index:
                symbol_found = check_adjacent_last_digit(data, column_iter, row_counter, column_limit, row_limit)
            else:
                symbol_found = check_adjacent_middle_digit(data, column_iter, row_counter, column_limit, row_limit)
            column_iter += 1
            if symbol_found == True:
                break
    return symbol_found

def main():
    data = []
    result = 0
    with open('input.txt', 'r') as iFile:
        data = iFile.readlines()
    row_counter = 0
    symbol_found = False
    row_limit = len(data)
    column_limit = len(data[0]) - 1

    while row_counter < len(data):
        number_str = ""
        column_iter = 0
        start_index = -1
        end_index = -1
        while column_iter < column_limit:
            if data[row_counter][column_iter].isdigit():
                if start_index == -1:
                    start_index = column_iter
                else:
                    end_index = column_iter
                # if a number is found, but
                if column_iter == column_limit - 1:
                    # if we've found a number, check all of the adjacent indexes
                    if start_index != -1:
                        # if we only have 1 digit
                        if end_index == -1:
                            end_index = start_index
                        for char in data[row_counter][start_index:end_index+1]:
                            number_str += char
                        symbol_found = check_adjacent_indexes(data, start_index,
                                                            end_index, row_counter,
                                                            column_limit, row_limit)
                        if symbol_found == True:
                            result += int(number_str)
                            print(int(number_str))
                        # reset control variables
                        start_index = -1
                        end_index = -1
                        number_str = ""
                        symbol_found = False
            else:
                # if we've found a number, check all of the adjacent indexes
                if start_index != -1:
                    # if we only have 1 digit
                    if end_index == -1:
                        end_index = start_index
                    for char in data[row_counter][start_index:end_index+1]:
                        number_str += char
                    symbol_found = check_adjacent_indexes(data, start_index,
                                                        end_index, row_counter,
                                                        column_limit, row_limit)
                    if symbol_found == True:
                        result += int(number_str)
                        print(int(number_str))
                    # reset control variables
                    start_index = -1
                    end_index = -1
                    number_str = ""
                    symbol_found = False
            column_iter += 1
        row_counter += 1
    print(result)


if __name__ == "__main__":
    main()