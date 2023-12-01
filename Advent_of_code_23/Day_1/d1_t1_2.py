import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

number_word_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

number_word = {
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
}


def main():
    result = 0
    first_num = 99
    second_num = 0
    coordinates = 0
    first_index_word = -1
    last_index_word = -1
    first_index_number = -1
    last_index_number = -1
    found_index = 0
    data = []
    with open("input1.txt", "r") as iFile:
        data = iFile.readlines()
    for line in data:
        for i in range(len(line)):
            if first_num == 99:
                if '0' < line[i] <= '9':
                        first_num = int(line[i])
                        first_index_number = i
                else:
                    found_number = -1
                    for number in number_word:
                        found_index = line[i:].find(number)
                        if found_index == 0:
                            first_index_word = found_index
                            found_number = number
                    if found_number != -1:
                        first_index_word += i
                        found_number = number_word_dict[found_number]
                        first_num = found_number
            else:
                if '0' <= line[i] <= '9':
                    if last_index_word != -1:
                        if i > last_index_word:
                            second_num = int(line[i])
                            last_index_number = i
                    else:
                        second_num = int(line[i])
                        last_index_number = i
                else:
                    found_number = -1
                    for number in number_word:
                        found_index = line[i:].rfind(number)
                        if found_index != -1:
                            if found_index > last_index_word:
                                last_index_word = found_index
                                found_number = number
                    if found_number != -1:
                        last_index_word += i
                        found_number = int(number_word_dict[found_number])
                        if last_index_number < last_index_word:
                            second_num = found_number
        if second_num == 0:
            second_num = first_num
        coordinates = first_num * 10 + second_num
        result += coordinates
        print(coordinates)
        first_num = 99
        second_num = 0
        coordinates = 0
        first_index_word = -1
        last_index_word = -1
        first_index_number = -1
        last_index_number = -1
        found_index = 0
    print(result)


if __name__ == "__main__":
    main()