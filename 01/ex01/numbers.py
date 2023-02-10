
def read_print_file():
    with open("numbers.txt") as f:
        content = f.readline()
        print(*content.rstrip("\n").split(","), sep ="\n")
if __name__ == "__main__":
    read_print_file()
