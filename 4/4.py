import re
input = open("4/input.txt", "r").read()

scratchcards = input.split('\n')

test_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

#PART 1 ------------

win_num_pattern = r':\s*([\d.]+(?:\s+[\d.]+)*)\s*[|]'

scratched_num_pattern = r'[|]\s*([\d.]+(?:\s+[\d.]+)*)\s*'

test = test_input.split('\n')

list_to_analyze = scratchcards

#iterate through the input
winning_numbers_list = list(map(lambda a: re.search(win_num_pattern, a).group(1).split(), list_to_analyze))
scratched_numbers_list = list(map(lambda a: re.search(scratched_num_pattern, a).group(1).split(), list_to_analyze))

points = 0
for win_nums, scratched_nums in zip(winning_numbers_list, scratched_numbers_list):
    card_points = 0
    for win_num in win_nums:
        try:
            scratched_nums.index(win_num)
            card_points = card_points * 2 if card_points > 0 else 1
        except ValueError:
            pass
    points += card_points

print(points)

#PART 2 ---------
cards = [1 for i in range(len(list_to_analyze))]
i = 0
while i < len(list_to_analyze):
    copy_num = 0
    for win_num in winning_numbers_list[i]:
        try:
            scratched_numbers_list[i].index(win_num)
            copy_num += 1
        except ValueError:
            pass
    for j in range(i+1, i+copy_num + 1):
        cards[j] += cards[i]
    i += 1

result = sum(cards)
print(result)