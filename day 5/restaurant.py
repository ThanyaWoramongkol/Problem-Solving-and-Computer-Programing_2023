"""Restaurant"""

def restaurant(cost, discount_cap, discount, spend):
    """    a bath, b >= a , discount(%) , buy more"""
    totle = cost + spend
    when_dis = totle * ((100-discount)/100)
    if cost == discount_cap:
        cost = cost * ((100-discount) / 100)
    interesting = cost - when_dis
    if totle >= discount_cap:
        if interesting < 0:
            print("No %.3f" % abs(interesting))
        elif interesting == 0:
            print("Yes")
        else:
            print("Yes %.3f" % abs(interesting))
    else:
        print("Yes")
restaurant(float(input()), float(input()), float(input()), float(input()))
