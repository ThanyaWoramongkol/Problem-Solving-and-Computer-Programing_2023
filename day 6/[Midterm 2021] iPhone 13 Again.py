"""iPhone"""
def mini(rom):
    """iPhone 13 mini"""
    if rom == "128 GB":
        return 25900
    elif rom == "256 GB":
        return 29900
    elif rom == "512 GB":
        return 37900
    else:
        return "Not Available"

def normal(rom):
    """iPhone 13"""
    if rom == "128 GB":
        return 29900
    elif rom == "256 GB":
        return 33900
    elif rom == "512 GB":
        return 41900
    else:
        return "Not Available"

def pro(rom):
    """iPhone 13 Pro"""
    if rom == "128 GB":
        return 38900
    elif rom == "256 GB":
        return 42900
    elif rom == "512 GB":
        return 50900
    elif rom == "1 TB":
        return 58900
    else:
        return "Not Available"

def promax(rom):
    """iPhone 13 Pro Max"""
    if rom == "128 GB":
        return 42900
    elif rom == "256 GB":
        return 46900
    elif rom == "512 GB":
        return 54900
    elif rom == "1 TB":
        return 62900
    else:
        return "Not Available"

def richy(gen, rom):
    """-"""
    if gen == "iPhone 13 mini":
        print(mini(rom))
    elif gen == "iPhone 13":
        print(normal(rom))
    elif gen == "iPhone 13 Pro":
        print(pro(rom))
    elif gen == "iPhone 13 Pro Max":
        print(promax(rom))
    else:
        print("Not Available")
richy(input(), input())
