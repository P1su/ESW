import numpy as np

class Block:
    def __init__(self, x, y):
        self.appearance= 'rectangle'       
        self.position = np.array([y*50, x*50, y*50+50, x*50+50]) 
        self.state = None