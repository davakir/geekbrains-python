numbers_with_titles = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}

with open('files/strings.txt') as file_obj:
    with open('files/strings_new.txt', 'w') as file_new:
        for line in file_obj.readlines():
            line = line.split(' - ')
            if line[0].lower() in numbers_with_titles.keys():
                line[0] = numbers_with_titles[line[0].lower()]

            line = ' - '.join(line)
            file_new.write(line)
