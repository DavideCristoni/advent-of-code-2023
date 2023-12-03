input = open("input.txt", "r").read()

# PART ONE --------

test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

test = test_input.split('\n')

games = input.split('\n')

bag = {"red":12, "green":13, "blue":14}

def isGameValid(game:str, bag:dict[str, int]=bag) -> bool:
    game_without_header = game[game.find(":") + 1:] # remove the "Game <num>:"
    list_of_draws = game_without_header.split(';') # separate every draw
    for draw in list_of_draws:
        cubes = draw.split(',') # separate the cubes per colour
        for number_and_color in cubes:
            cube = number_and_color.split() # separate the number of cubes from the colour
            count = int(cube[0])
            colour = cube[1]
            if bag[colour] < count : # if the bag has less cubes of the colour selected
                return False         # that game is not possible, so don't count it
    return True

games_sum = 0

for i in range(0, len(games)):
    if isGameValid(games[i]):
        games_sum += i + 1

print(f"games sum = {games_sum}")

# PART 2 ----------

def minSetOfCubes(game:str) -> int:
    min_set = {"red":[], "green":[], "blue":[]}
    game_without_header = game[game.find(":") + 1:] # remove the "Game <num>:"
    list_of_draws = game_without_header.split(';') # separate every draw
    for draw in list_of_draws:
        cubes = draw.split(',') # separate the cubes per colour
        for number_and_color in cubes:
            cube = number_and_color.split() # separate the number of cubes from the colour
            count = int(cube[0])
            colour = cube[1]
            min_set[colour].append(count)
    min_red = max(min_set["red"])
    min_green = max(min_set["green"])
    min_blue = max(min_set["blue"])
    return min_red * min_green * min_blue

min_set_pow_sum = 0

for i in range(0, len(games)):
    min_set_pow_sum += minSetOfCubes(games[i])


print(f"min set power sum = {min_set_pow_sum}")