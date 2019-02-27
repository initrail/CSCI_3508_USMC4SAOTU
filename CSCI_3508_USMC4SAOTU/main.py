from data_reader import data_reader as dr
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('height', type=int, help='an integer for the height of the grid')
    parser.add_argument('width', type=int, help='an integer for the width of the grid')

    args = parser.parse_args()

    height = args.__dict__["height"]
    width = args.__dict__["width"]

    print("height = ", flush=True, end="")
    print(args.__dict__["height"])
    print("width = ", flush=True, end="")
    print(args.__dict__["width"])

    newReader = dr(width, height)
    print(newReader.readGrid())

if __name__ == '__main__':
    main()