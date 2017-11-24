def score(game):
    NUMBER_OF_FRAMES = 10
    NUMBER_OF_PINS = 10
    OUTCOMES = {"strike": ("X", "x"), "spare": "/"}

    result = 0
    last = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):
        if game[i] == OUTCOMES["spare"]:
            result += NUMBER_OF_PINS - last
        else:
            result += get_value(game[i])
        if frame < NUMBER_OF_FRAMES and get_value(game[i]) == NUMBER_OF_PINS:
            result += get_value(game[i + 1])
            if game[i] in OUTCOMES["strike"]:
                if game[i + 2] == OUTCOMES["spare"]:
                    result += NUMBER_OF_PINS - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half or game[i] in OUTCOMES["strike"]:
            frame += 1
            in_first_half = True
        else:
            in_first_half = False

    return result


def get_value(char):
    POSSIBLE_CHARS = {"numbers": ('1', '2', '3', '4', '5', '6', '7', '8', '9'),
                      "strike": ("X", "x"), "spare": "/", "miss": "-"}

    if char in POSSIBLE_CHARS["numbers"]:
        return int(char)
    elif char in POSSIBLE_CHARS["strike"] or char == POSSIBLE_CHARS["spare"]:
        return 10
    elif char == POSSIBLE_CHARS["miss"]:
        return 0
    else:
        raise ValueError()
