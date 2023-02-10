import sys

def capital_city():
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
        sys.exit()
    param = sys.argv[1]
    if len(sys.argv[1]) == 2:
        exit()
    for x, y in states.items():
        if x == param:
            param = y
    for x, y in capital_cities.items():
        if x == param:
            print(y)
            exit(0)
    print('Unknown state')   
            
if __name__ == "__main__":
    capital_city()
