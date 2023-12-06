import numpy as np


class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = 'move'
        self.position = np.array([width, height, width + 30, height + 30])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"
        self.dir = 'none'
        self.block = 'none'
        self.item = 'none'

    def move(self, blocks, command = None):
        if command == None:
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command=='up_pressed':
               
                self.position[1] -= 3
                self.position[3] -= 3
                self.dir = "up"

            if command=='down_pressed':
                self.position[1] += 3
                self.position[3] += 3
                self.dir = "down"

            if command=='left_pressed':
                self.position[0] -= 3
                self.position[2] -= 3
                self.dir = "left"
                
            if command=='right_pressed':
                self.position[0] += 3
                self.position[2] += 3
                self.dir = "right"
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 
        
    def check_flag(self, flag):
        check = self.overlap(self.position, flag.position)
        if check:
            flag.state = "fin"
    
    
    
    
    def check_item(self, item):
        check = self.overlap(self.position, item.position)
        
        if check:
            item.state = "drop"   
            self.item ='ready'
            
   
            
    def check_block(self, blocks):
        newPosition=[0,0,0,0]
        for block in blocks:
            newPosition[0] = block.position[0]-10
            newPosition[1] = block.position[1]+10
            newPosition[2] = block.position[2]-10
            newPosition[3] = block.position[3]+10
            
            check = self.overlap(self.position, newPosition)
            if check:
                self.block = "block"
                break
            else:
                self.block = None
        
            
    def overlap(self, ego_position, other_position):
        
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                 and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]