import sys

def verify(regularword, upword, states, capital_cities):
    for x, y in capital_cities.items():
        if y.upper() ==  upword:
            checker = x
            for x, y in states.items():
                if y.upper() == checker:
                    print(regularword.title(), "is the capital of", x)
                    return()
    for x, y in states.items():
        if x.upper() == upword:
            checker = y
            for x, y in capital_cities.items():
                if x.upper() == checker:
                    print(y, "is the capital of", regularword.title())
                    return()
    print(regularword,"is neither a capital city nor a state")

def all_in():
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
        exit(0)
    check = ',,'
    if check in sys.argv[1]:
        exit(0)
            
    splitted = sys.argv[1].split(',')
    for i in splitted:
        upword = i.strip().upper()
        if (upword != ""):
            verify(i.strip(), upword, states, capital_cities)


if __name__ == "__main__":
    all_in()
