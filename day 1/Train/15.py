"""Train"""
def main(txt1, txt2, count):
    """_"""
    txt_out = txt1+txt2
    print("%s\n%s" % (txt_out, txt_out * count))
main(input(), input(), int(input()))
