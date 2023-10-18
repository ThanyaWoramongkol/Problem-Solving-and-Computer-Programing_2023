"""Donut"""
#  a baht, If buy donut b pieces, Free c pieces, Buy d piece
def main(cost, free_condition, free, jumnuan):
    """_"""
    jumnuan_free = (jumnuan % free_condition) * free
    jumnuan_buy = jumnuan - jumnuan_free
    cost_spend = cost * (jumnuan_buy)
    donut_get = jumnuan_free + jumnuan_buy
    if jumnuan < free_condition:
        print(jumnuan * cost, jumnuan)
    else:
        print(cost_spend, donut_get)
main(int(input()), int(input()), int(input()), int(input()))
