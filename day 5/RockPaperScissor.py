"""RockPaperScissor"""
def score(pointa, pointb):
    """-"""
    if pointa > pointb:
        return "A win %d-%d" % (pointa, pointb)
    elif pointa < pointb:
        return "B win %d-%d" % (pointb, pointa)
    else:
        return "DRAW %d" % pointa

def win(rotation):
    """-"""
    score_a = 0
    score_b = 0

    for i in range(0, len(rotation), 2):
        if rotation[i] == rotation[i+1]:
            continue
        elif rotation[i] == 'R':
            if rotation[i+1] == 'P':
                score_b += 1
            else:
                score_a += 1
        elif rotation[i] == 'P':
            if rotation[i+1] == 'R':
                score_a += 1
            else:
                score_b += 1
        elif rotation[i] == 'S':
            if rotation[i+1] == 'R':
                score_b += 1
            else:
                score_a += 1
    return score(score_a, score_b)
print(win(input()))
