import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14

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
                if int(one_set_of_cubes[counter]) > RED_THRESHOLD:
                    impossible_game = True
            elif one_set_of_cubes[counter+1] == 'green':
                if int(one_set_of_cubes[counter]) > GREEN_THRESHOLD:
                    impossible_game = True
            else:
                if int(one_set_of_cubes[counter]) > BLUE_THRESHOLD:
                    impossible_game = True
            # if the game is impossible, move to the next line
            if impossible_game == True:
                break
            counter += 2
        if impossible_game == True:
            break
        else:
            continue
    if impossible_game == False:
        return game_template['id']
    else:
        return 0

    print([processed_line])

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