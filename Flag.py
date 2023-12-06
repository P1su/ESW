import numpy as np

class Flag:
    def __init__(self, x,y):
        self.appearance = 'rectangle'
        self.state = 'yet'
        self.position = np.array([x*50, y * 50, x*50 + 50, y*50+50])#왼쪽 위와 오른쪽 아래