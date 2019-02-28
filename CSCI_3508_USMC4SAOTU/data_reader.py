import sys,json
import numpy as np

class data_reader:
    def __init__(self, width, height):
        self.grid = np.zeros((height,), dtype=int)
        self.width = width
        self.height = height
        self.readGrid()

    def readGrid(self):
        with open('test.json') as f:
            data = json.load(f)

#        data = json.load(sys.stdin)
        for column in data['grid']:
            g = np.asarray(column)
            self.grid = np.column_stack((self.grid, g))

        self.grid = np.delete(self.grid, 0,axis=1)

        return self.grid