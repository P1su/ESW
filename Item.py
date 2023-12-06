import numpy as np

class Item:
    def __init__(self, x, y):
        self.appearance = 'rectangle'
        self.state = 'none'
        self.position = np.array([x*50, y*50, x*50+50, y*50+50]) 