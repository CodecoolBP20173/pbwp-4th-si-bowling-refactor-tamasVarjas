def score(game):
    OUTCOMES = {"strike": ("X", "x"), "spare": "/"}
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == OUTCOMES["spare"]:
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == OUTCOMES["spare"]:
                result += get_value(game[i + 1])
            elif game[i] in OUTCOMES["strike"]:
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] in OUTCOMES["strike"]:
            in_first_half = True
            frame += 1
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
