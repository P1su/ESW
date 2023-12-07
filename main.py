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
    
def main():
    global start
    global map
    
    color = "#F12FF1"
    blocks = []
    shoots = []
    joystick = Joystick()
    image = Image.new("RGB", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(image)
    warrior = Image.open("/home/kau-esw/EswEscape/ESW/ESW/warrior.png")
    warriorT= Image.open("/home/kau-esw/EswEscape/ESW/ESW/warriorBack.png")
    warriorL = Image.open("/home/kau-esw/EswEscape/ESW/ESW/warriorLeft.png")
    warriorR= Image.open("/home/kau-esw/EswEscape/ESW/ESW/warriorRight.png")
    flagImg = Image.open("/home/kau-esw/EswEscape/ESW/ESW/flag.png")
    itemImg = Image.open("/home/kau-esw/EswEscape/ESW/ESW/Item.png")
    blockImg = Image.open("/home/kau-esw/EswEscape/ESW/ESW/block.png")
    fireImg = Image.open("/home/kau-esw/EswEscape/ESW/ESW/fireball.png")
    titleImg = Image.open("/home/kau-esw/EswEscape/ESW/ESW/title.png")
   
    
    print(start)
    
    if start == 1:
        map = map3
    elif start == 2:
        map = map2      
    elif start ==3:
        map = map3
    elif start ==4:
        draw.rectangle((0,0,1000, 1000), fill = (105,105,105,0))
        draw.text((80, 120), "GAME CLEAR!!!!!",fill =(255, 0, 0, 0))
        joystick.disp.image(image)
        exit()
         
    for x in range(len(map)):
            
        for y in range(len(map)):
                
            if(map[y][x] == 1):
                block = Block(y,x)
                blocks.append(block)
                    
            elif map[y][x] == 2:
                character = Character(x*50, y*50)
                
            elif map[y][x] == 3:
                
                flag = Flag(x,y)
            elif map[y][x] == 4:
               
                item = Item(x,y)
               
    flag.state == None            
    
    while True:
        command = None
        
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'
            color = "#01FF3F"
            
            for block in blocks:
                block.position[1]+=10
                block.position[3]+=10
                
            flag.position[1]+=10
            flag.position[3]+=10
            item.position[1]+=10
            item.position[3]+=10
            
        if not joystick.button_D.value:  # down pressed
            command = 'down_pressed'
            color = "#F12FF1"
            
            for block in blocks:
                block.position[1]-=10
                block.position[3]-=10
                
            flag.position[1]-=10
            flag.position[3]-=10
            item.position[1]-=10
            item.position[3]-=10   

        if not joystick.button_L.value:  # left pressed
            command = 'left_pressed'
            color = "#FF0000"
            
            for block in blocks:
                block.position[0]+=10
                block.position[2]+=10
                
            flag.position[0]+=10
            flag.position[2]+=10
            item.position[0]+=10
            item.position[2]+=10

        if not joystick.button_R.value:  # right pressed
            command = 'right_pressed'
            color = "#FFFF12"
            
            for block in blocks:
                block.position[0]-=10
                block.position[2]-=10
            
            flag.position[0]-=10
            flag.position[2]-=10
            item.position[0]-=10
            item.position[2]-=10
        
        if not joystick.button_A.value:
            if character.item == 'ready':
                shoot = Shoot(character.center, command)
                shoots.append(shoot)
                character.item = None
                
        if not joystick.button_B.value:
            start = 1
                
        if start == 0 :
            draw.bitmap((20,40), titleImg, fill = (0,250,154))
            draw.text((80, 200), "PRESS 'B' TO START",fill =(255, 0, 0, 0))      
        
        else  :
            
            character.move(blocks, command)
            for shoot in shoots:
                shoot.collision_check(blocks)
                shoot.move()
                if shoot.state == 'hit':
                    shoots.clear()
                    
            draw.rectangle((0,0,1000, 1000), fill = (10,0,0,0))#배경 그리기
            
            for block in blocks: #벽 그리기
               
                if block.state != 'destroy':
                    draw.bitmap((block.position[0],block.position[1]),blockImg, fill = (105,105,105) )
            
            if item.state != 'drop':
                draw.bitmap((item.position[0]+5,item.position[1]+5), itemImg, fill = (60,179,113))#아이템 그리기
            
            draw.bitmap((flag.position[0], flag.position[1]), flagImg, fill =(0,0,200))#도착지점 그리기
            
            if character.dir == 'down' or character.dir == 'none':#캐릭터 그리기
                draw.bitmap((character.position[0],character.position[1]), warrior, fill = color)
            elif character.dir == 'up':
                draw.bitmap((character.position[0],character.position[1]), warriorT, fill = color)
            elif character.dir == 'left':
                draw.bitmap((character.position[0],character.position[1]), warriorL, fill = color)
            elif character.dir == 'right':
                draw.bitmap((character.position[0],character.position[1]), warriorR, fill = color)    
               
            for shoot in shoots:
                if shoot.state != 'hit':
                    draw.bitmap((shoot.position[0], shoot.position[1]),fireImg ,fill = (255, 99, 71))#공을 날려 벽 부수기
            
            character.check_item(item)#아이템 체크
            character.check_flag(flag)
            
            if flag.state == 'fin': #도착하면 클리어 문구 띄우기
                draw.text((1, 200), "STAGE CLEAR",fill =(255, 0, 0, 0)) 
                
                time.sleep(2)
                start +=1
                main()
            
                      
        joystick.disp.image(image)
        
        
            
if __name__ == '__main__':
    
    main()