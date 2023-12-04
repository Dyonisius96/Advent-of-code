import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def calculate_card_worth(card:str):
    card_worth = 0
    data = card.split(':')
    data = data[1].split('|')
    processed_data = {
        'winning numbers': data[0].split(),
        'numbers': data[1].split()
    }

    for number in processed_data['numbers']:
        for winning_number in processed_data['winning numbers']:
            if number == winning_number:
                if card_worth == 0:
                    card_worth = 1
                else:
                    card_worth *= 2
                # the number was already found
                processed_data['winning numbers'].remove(winning_number)
                break
    return card_worth

def main():
    data = []
    result = 0
    with open('input.txt', 'r') as iFile:
        data = iFile.readlines()

    for card in data:
        card_worth = calculate_card_worth(card)
        print(card_worth)
        result += card_worth
    print(result)

if __name__ == "__main__":
    main()