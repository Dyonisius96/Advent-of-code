import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
    data = []
    with open("input1.txt", "r") as iFile:
        data = iFile.readlines()
    for line in data:
        for char in line:
            if first_num == 99:
                if '0' <= char <= '9':
                    first_num = int(char)
            else:
                if '0' <= char <= '9':
                    second_num = int(char)
        if second_num == 0:
            second_num = first_num
        coordinates = first_num * 10 + second_num
        result += coordinates
        print(coordinates)
        coordinates = 0
        first_num = 99
        second_num = 0
    print(result)


if __name__ == "__main__":
    main()