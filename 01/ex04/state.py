import sys

def state():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(sys.argv) != 2:
        exit()
    param = sys.argv[1]
    if len(sys.argv[1]) == 2:
        exit()
    for x, y in capital_cities.items():
        if y == param:
            param = x
    for x, y in states.items():
        if y == param:
            print(x)
            exit(0)
    print('Unknown capital city')           
if __name__ == "__main__":
    state()
