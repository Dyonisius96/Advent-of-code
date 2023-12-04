import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def calculate_card_worth(card:str):
    matching_numbers = 0
    data = card.split(':')
    data = data[1].split('|')
    processed_data = {
        'winning numbers': data[0].split(),
        'numbers': data[1].split()
    }

    for number in processed_data['numbers']:
        for winning_number in processed_data['winning numbers']:
            if number == winning_number:
                matching_numbers += 1
                # the number was already found
                processed_data['winning numbers'].remove(winning_number)
                break
    return matching_numbers

def main():
    data = []
    result = 0
    card_count = {}
    with open('input.txt', 'r') as iFile:
        data = iFile.readlines()
    for line in data:
        card_count[int(line.split(':')[0].split()[1])] = 1

    for iter in range(len(data)):
        matching_numbers = calculate_card_worth(data[iter])
        if matching_numbers:
            for id in range(matching_numbers):
                card_count[iter+1+id+1] += card_count[iter+1]

    for id in range(len(card_count)):
        result += card_count[id+1]

    print(result)

if __name__ == "__main__":
    main()