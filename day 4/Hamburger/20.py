"""Hamburger"""

def burger_king(bread, kanom_pang):
    """meat = (bread + kanom_pang)* 2"""
    print("|" * bread, end="")
    print("**" * (bread + kanom_pang), end="")
    print("|" * kanom_pang, end="")

burger_king(int(input()), int(input()))
