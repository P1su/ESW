from PIL import Image, ImageDraw, ImageFont
import time
import random
import pygame
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Character import Character
from map1 import map1
from Flag import Flag
from Block import Block
from Item import Item
from map2 import map2
from Shoot import Shoot
from map3 import map3
    
#hieght, width는 각각 240

start = 0
map = map1
    
def setStage(map):
    circle_color = "#F12FF1"
    blocks = []
    shoots = []
    get_flag = False
    joystick = Joystick()
    image = Image.new("RGB", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(image)

def main():
    global start
    global map
    circle_color = "#F12FF1"
    blocks = []
    shoots = []
    get_flag = False
    joystick = Joystick()
    image = Image.new("RGB", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(image)
  #  img = Image.open("/home/kau-esw/EswEscape/test.png")
  #  imgDraw = ImageDraw.Draw(img)
    
    
    draw.rectangle((0,0,1000, 1000), fill = (255,255,255,0))
    
  #  imgDraw.bitmap((100,100), img, fill = (255,255,255,0))
  #  draw.bitmap((1000,1000),img, fill = (255,255,255,0))
    
    
    if start == 1:
        map = map1
    elif start == 2:
        map = map2      
    elif start ==3:
        map = map3
         
             
    for x in range(len(map)):
            
        for y in range(len(map)):
                
            if(map[y][x] == 1):
                block = Block(y,x)
                blocks.append(block)
                    
            elif map[y][x] == 2:
                my_circle = Character(x*50, y*50)
            elif map[y][x] == 3:
                
                flag = Flag(x,y)
            elif map[y][x] == 4:
               item = Item(x,y)
                
    
    while True:
        command = None
        
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'
            circle_color = "#01FF3F"
            
            for block in blocks:
                block.position[1]+=10
                block.position[3]+=10
                
            flag.position[1]+=10
            flag.position[3]+=10
            item.position[1]+=10
            item.position[3]+=10
            
        if not joystick.button_D.value:  # down pressed
            command = 'down_pressed'
            circle_color = "#F12FF1"
            
            for block in blocks:
                block.position[1]-=10
                block.position[3]-=10
                
            flag.position[1]-=10
            flag.position[3]-=10
            item.position[1]-=10
            item.position[3]-=10   

        if not joystick.button_L.value:  # left pressed
            command = 'left_pressed'
            circle_color = "#FF0000"
            
            for block in blocks:
                block.position[0]+=10
                block.position[2]+=10
                
            flag.position[0]+=10
            flag.position[2]+=10
            item.position[0]+=10
            item.position[2]+=10

        if not joystick.button_R.value:  # right pressed
            command = 'right_pressed'
            circle_color = "#FFFF12"
            
            for block in blocks:
                block.position[0]-=10
                block.position[2]-=10
            
            flag.position[0]-=10
            flag.position[2]-=10
            item.position[0]-=10
            item.position[2]-=10
        
        if not joystick.button_A.value:
            if my_circle.item == 'ready':
                shoot = Shoot(my_circle.center, command)
                shoots.append(shoot)
                my_circle.item = None
                
        if not joystick.button_B.value:
            start = 1
                
        if start == 0 :
            draw.text((80, 120), "PRESS 'B' TO START",fill =(255, 0, 0, 0))        
        elif start == 4:
            draw.rectangle((0,0,1000, 1000), fill = (255,255,255,0))

            draw.text((80, 120), "GAME CLEAR!!!!!",fill =(255, 0, 0, 0))   
            break       
        else  :
            print(my_circle.center)
            my_circle.move(blocks, command)
            
            for shoot in shoots:
                shoot.collision_check(blocks)
                shoot.move()
                if shoot.state == 'hit':
                    shoots.clear()
                    
            draw.rectangle((0,0,1000, 1000), fill = (255,255,255,0))
            
            
            for block in blocks: #벽 그리기
                if block.state != 'destroy':
                    draw.rectangle(tuple(block.position),outline = "#FFFFFF", fill = "#001FFF" )
            
            my_circle.check_item(item)#아이템 체크
            
            if item.state != 'drop':
                draw.rectangle(tuple(item.position), outline = "#FFFFFF", fill = (40,50,100))#아이템 그리기
                
            my_circle.check_block(blocks)
            print(my_circle.block)
            
        # print(my_circle.position[0], my_circle.position[1], my_circle.position[2], my_circle.position[3])        
            # 아이템 그리기
            
            draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = circle_color) #캐릭터 그리기
            
            draw.rectangle(tuple(flag.position), outline = "#FFFFFF", fill =(0,0,0))#도착지점 그리기
            
            for shoot in shoots:
                if shoot.state != 'hit':
                    draw.rectangle(tuple(shoot.position), fill = (0, 0, 255))

            
            my_circle.check_flag(flag)
            
            if flag.state == 'fin': #도착하면 클리어 문구 띄우기
                draw.text((1, 200), "STAGE CLEAR",fill =(255, 0, 0, 0)) 
                
                time.sleep(2)
                start +=1
                main()
                
                
                                         
        joystick.disp.image(image)
        
        
            
if __name__ == '__main__':
    
    main()