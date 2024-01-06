import re

VERBAL_DIGITS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

DIGITS_PATTERN = "zero|one|two|three|four|five|six|seven|eight|nine"


def get_matches(path):
    pattern = re.compile(
        fr"^.*?(?=(\d|{DIGITS_PATTERN})).*(\d|{DIGITS_PATTERN})", re.MULTILINE,
    )
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        matches = re.findall(pattern, content)
        return matches


def interpret_match(match: (str, str)) -> int:
    left = VERBAL_DIGITS[match[0]] if match[0] in VERBAL_DIGITS else match[0]
    right = VERBAL_DIGITS[match[1]] if match[1] in VERBAL_DIGITS else match[1]
    return int(left + right)


def sum_matches(matches):
    total = 0
    for match in matches:
        total += interpret_match(match)
    return total


if __name__ == "__main__":
    matches = get_matches("data.txt")
    print(matches)
    print(sum_matches(matches))
