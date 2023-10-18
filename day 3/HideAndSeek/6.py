"""HideAndSeek"""

def main(start, finish, jumper):
    """start to finish by jumper"""
    for i in range(start, finish, jumper):
        print(i)
main(int(input()), int(input()), int(input()))
