"""Bill"""

def cost(money):
    """_"""
    service = money * 0.1
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    vat = (money + service) * 0.07
    spend = money + service + vat
    print("%.2f" % spend)
cost(int(input()))
