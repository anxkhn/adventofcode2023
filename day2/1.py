import re

games_data = {}
game_pattern = re.compile(r"Game (\d+): (.+)$")

with open('input.txt', 'r') as f:
    for line in f:
        match = game_pattern.match(line.strip())
        if match:
            game_number, game_details = match.groups()

            color_pattern = re.compile(r"(\d+) (\w+|\w+\s\w+)")
            
            game_list = []
            for set_details in game_details.split(';'):
                set_dict = {}
                for count, color in color_pattern.findall(set_details):
                    set_dict[color] = int(count)
                game_list.append(set_dict)

            games_data[int(game_number)] = game_list

print(games_data)

total = []

for game_key in games_data.keys():
    flag = True
    for i in games_data[game_key]:
        red = i.get("red", 0)
        blue = i.get("blue", 0)
        green = i.get("green", 0)
        if red > 12 or green > 13 or blue > 14:
            flag = False
    if flag == True:
        total.append(game_key)

print(total)
print(sum(total))
