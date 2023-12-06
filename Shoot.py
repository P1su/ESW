import numpy as np

class Shoot:
    def __init__(self, position, command):
        self.appearance = 'rectangl'
        self.speed = 10
        self.position = np.array([position[0]-2, position[1]-2, position[0]+2, position[1]+2])
        self.state = None
        self.outline = "#0000FF"
        self.dir = None  
              
        if command == 'up_pressed':
            self.dir = 'up'
        if command == 'down_pressed':
            self.dir = 'down'
        if command == 'left_pressed':
            self.dir = 'left'
        if command == 'right_pressed':
            self.dir = 'right'
       
    def move(self):
        
        if self.dir == 'up':
            self.position[1] -= self.speed
            self.position[3] -= self.speed
            
        if self.dir == 'down':
            self.position[1] += self.speed
            self.position[3] += self.speed
        
        if self.dir == 'left':
            self.position[0] -= self.speed
            self.position[2] -= self.speed
        
        if self.dir == 'right':
            self.position[0] += self.speed
            self.position[2] += self.speed
            

    def collision_check(self, blocks):
        for block in blocks:
            collision = self.overlap(self.position, block.position)
            
            
            if collision:
                block.state = 'destroy'
                self.state = 'hit'
                break

    def overlap(self, ego_position, other_position):
        
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                 and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]