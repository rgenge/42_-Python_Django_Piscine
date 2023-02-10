from local_lib.path import Path

def main():
    try:
        Path('folder').mkdir()
    except Exception as e:
        print(e)
    filename = Path('folder/file')
    filename.touch()
    filename.write_text('my program')
    print(filename.read_text())

if __name__ == '__main__':
    main()