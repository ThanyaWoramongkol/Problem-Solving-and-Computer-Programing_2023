"""Pro"""

def promotion(mar, jai, cost, jumnuan):
    """-"""
    print(((jumnuan//mar)*jai)*cost + (jumnuan%mar)*cost)
promotion(int(input()), int(input()), int(input()), int(input()))
