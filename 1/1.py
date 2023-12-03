# INPUT --------------
calibration_value = open("input.txt", "r").read()

# PART ONE --------------
def getFirstNumber(calibration_line:str):
    for character in calibration_line:
        if character.isdigit():
            return character


def getLastNumber(calibration_line:str):
    reverse_line = calibration_line[::-1] #reverse the string
    for character in reverse_line:
        if character.isdigit():
            return character


calibration_list = calibration_value.split('\n')
calibration_sum = 0

for line in calibration_list:
    calibration_sum += int(getFirstNumber(line) + getLastNumber(line))

#note: the two functions do the same thing, the getLastNumber just reverts the string before iterating it. 
#      It is sufficient to have just the first one, feeding the reversed string to get the last number

print(f"First step: {calibration_sum}")

# PART TWO -------------

test = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

test_list = test.split('\n')

number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def getFirstDigitPlus(calibration_line:str):
    matching_numbers = []
    indexes = []
    for character in calibration_line:
        if character.isdigit():
            return character
        if matching_numbers:
            i = 0
            while i < len (matching_numbers):
                if character != matching_numbers[i][indexes[i]]:
                    indexes.pop(i)
                    matching_numbers.pop(i)
                else:
                    indexes[i] += 1
                    if len(matching_numbers[i]) == indexes[i]:
                        return str(number.index(matching_numbers[i]) + 1)
                    i += 1
        for letter_number in number:
            if character == letter_number[0]:
                matching_numbers.append(letter_number)
                indexes.append(1)

rebmun = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def getLastDigitPlus(calibration_line:str):
    reversed = calibration_line[::-1]
    matching_numbers = []
    indexes = []
    for character in reversed:
        if character.isdigit():
            return character
        if matching_numbers:
            i = 0
            while i < len (matching_numbers):
                if character != matching_numbers[i][indexes[i]]:
                    indexes.pop(i)
                    matching_numbers.pop(i)
                else:
                    indexes[i] += 1
                    if len(matching_numbers[i]) == indexes[i]:
                        return str(rebmun.index(matching_numbers[i]) + 1)
                    i += 1
        for letter_number in rebmun:
            if character == letter_number[0]:
                matching_numbers.append(letter_number)
                indexes.append(1)


calibration_sum = 0

for line in calibration_list:
    code_found = int(getFirstDigitPlus(line) + getLastDigitPlus(line))
    # print(f"line: {line} code: {code_found}")
    calibration_sum += code_found

print(f"Second step: {calibration_sum}")