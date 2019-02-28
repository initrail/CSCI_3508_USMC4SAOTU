from data_reader import data_reader as dr
import move_selector_naive as mv
import argparse, sys

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('height', type=int, help='an integer for the height of the grid', default=6, nargs='?')
    parser.add_argument('width', type=int, help='an integer for the width of the grid', default=7, nargs='?')

    args = parser.parse_args()

    height = args.__dict__["height"]
    width = args.__dict__["width"]

    print("height = ", flush=True, end="")
    print(args.__dict__["height"])
    print("width = ", flush=True, end="")
    print(args.__dict__["width"])

    newReader = dr(width, height)
    print(newReader.grid)
    move = mv.randMove(newReader)
    # we just need to put our move in stdout right?
    sys.stdout.write(str(move))



if __name__ == '__main__':
    main()