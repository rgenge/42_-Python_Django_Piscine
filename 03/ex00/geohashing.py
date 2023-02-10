import sys
import antigravity

def main():
    if(len(sys.argv) != 4):
        print ("You must type latitude, longitude, date")
        exit(0)
    try:
        latitude = float(sys.argv[1])
    except:
        print("type float latitude")
    try:
        longitude = float(sys.argv[2])
    except:
        print("type float longitude")
    try:
        date = sys.argv[3].encode()
    except:
        print("type date string")
    antigravity.geohash(latitude, longitude, date)

if __name__ == "__main__":
    main()