import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_if_possible(game_line :str):
    game_template = {
        'red': 0,
        'green': 0,
        'blue': 0,
        'id': 0
    }
    games = []
    impossible_game = False
    processed_line = game_line.split(':')
    processed_line[0] = processed_line[0].removeprefix("Game ")
    # store ID of the game
    game_template['id'] = int(processed_line[0])
    # remove first one
    processed_line = processed_line[1:]
    processed_line = processed_line[0].split(';')
    for line in processed_line:
        one_set_of_cubes = line.split()
        for id in range(len(one_set_of_cubes)):
            one_set_of_cubes[id] = one_set_of_cubes[id].removesuffix(',')
        counter = 0
        while counter < (len(one_set_of_cubes) - 1):
            if one_set_of_cubes[counter+1] == 'red':
                if int(one_set_of_cubes[counter]) > game_template['red']:
                    game_template['red'] = int(one_set_of_cubes[counter])
            elif one_set_of_cubes[counter+1] == 'green':
                if int(one_set_of_cubes[counter]) > game_template['green']:
                    game_template['green'] = int(one_set_of_cubes[counter])
            else:
                if int(one_set_of_cubes[counter]) > game_template['blue']:
                    game_template['blue'] = int(one_set_of_cubes[counter])
            counter += 2
    power_of_set = game_template['blue'] * game_template['red'] * game_template['green']
    print(power_of_set)
    return power_of_set


def main():
    result = 0
    data = []

    with open("input1.txt" , "r") as iFile:
        data = iFile.readlines()
    for line in data:
        result += check_if_possible(line)
    print(result)

if __name__ == "__main__":
    main()