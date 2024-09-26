"""Volleyball"""
def score(set_ti, team1, team2, won):
    """-"""
    if not won:
        print("Set %d: A(%d) | B(%d)" % (set_ti, team1, team2))
        print("The game has not finished yet.")
    else:
        print("Set %d: A(%d) | B(%d)" % (set_ti, team1, team2))

def volley(match):
    """-"""
    a_win = 0
    b_win = 0
    set_ti = 1
    count = 0
    won = False
    draw = False
    last = False
    for win in match:
        if win == "A":
            a_win += 1
        elif win == "B":
            b_win += 1
        if count == len(match):
            last = True

        if a_win == 24 and b_win == 24:
            draw = True
        if abs(a_win - b_win) == 2 and draw:
            won = True
            score(set_ti, a_win, b_win, won)
        elif (a_win == 25 or b_win == 25) and (not draw):
            won = True
            score(set_ti, a_win, b_win, won)
        elif last:
            score(set_ti, a_win, b_win, won)
        count += 1

volley(input())            