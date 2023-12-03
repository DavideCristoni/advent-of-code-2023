import re
input = open("3/input.txt", "r").read()

engine_schematic = input.split('\n')

test_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

test = test_input.split('\n')

# PART ONE ---------

matrix = engine_schematic
engine_sum = 0
i= 0

while i < len(matrix):
    matches = re.finditer(r"\d+", matrix[i])
    for sliced in matches:
        start = sliced.start()
        start = start if start == 0 else start - 1
        end =  sliced.end()
        end = end if end == len(matrix[i]) else end + 1
        top = i if i == 0 else i - 1
        bottom = i if i == (len(matrix) - 1) else i + 1
        sub_matrix = matrix[top : bottom+1]
        sub_matrix = list(map(lambda line : line[start:end] , sub_matrix))
        substring = ''.join(sub_matrix)
        substring = substring.replace(sliced.group(),'').strip('.')
        if ( len(substring) > 0 ) and ( not substring.isdigit() ):
            engine_sum += int(sliced.group())
        j = end - 1
    i += 1

print(f"engine sum = {engine_sum}")

# PART TWO --------

def findAllStars(schematic:list[str]) -> list[list[re.Match[str]]]:
    result = []
    for line in schematic:
        matches = list(re.finditer(r"[*]", line))
        result.append(matches)
    return result

def findAllNumbers(schematic:list[str]) -> list[list[re.Match[str]]]:
    result = []
    for line in schematic:
        matches = list(re.finditer(r"\d+", line))
        result.append(matches)
    return result

stars = findAllStars(matrix)
numbers = findAllNumbers(matrix)
i = 0
gear_ratio = 0
while i < len(matrix):
    for star in stars[i]:
        count = []
        start = i if i == 0 else i-1
        end = i if i == len(matrix) else i+1
        number_list = [item for sublist in numbers[start:end+1] for item in sublist]
        # number_list = numbers[start:end+1]
        for number in number_list:
            if number.start() <= star.end() and number.end() >= star.start():
                count.append(int(number.group()))
        if len(count) == 2:
            gear_ratio += count[0] * count[1]
    i += 1

print(f"gear ratio = {gear_ratio}")