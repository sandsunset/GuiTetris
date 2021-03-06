import pygame
import time
from pygame import Rect
from random import randrange
from sys import stdout

pygame.init()

red = (226, 0, 0)
orange = (237, 181, 0)
yellow = (247, 247, 0)
green = (0, 229, 11)
light_blue = (0, 232, 232)
blue = (3, 0, 232)
purple = (187, 0, 234)
black = (0, 0, 0)
white = (255, 255, 255)

delay = 0.6

def draw_rect(x,y):
    pygame.draw.rect(screen, white, [x, y, 20, 20], 1)
    return None

def draw_color_rect(color, x, y):
    pygame.draw.rect(screen, color, [x, y, 20, 20], 1)

def stop_block_at_edge(info):
    coordinate = info['coordinate']

    for cr in coordinate:
        coordinateX = cr[0]
        coordinateY = cr[1]

        if coordinateX < 23 or coordinateX > 250:
            return True
        elif coordinateY > 433:
            return True
        else:
            continue

def random_type(type_dict):
    random_number = randrange(1,8)
    ran_type = type_dict[random_number]

    str_ran_type = str(ran_type)
    str_type = str_ran_type[20:26]

    return ran_type, str_type


class fall_time:
    def __init__(self):
        self.stamp = time.time()
        return None

    def check(self, current_time):
        self.current_time = time.time()
        if int(self.current_time) - int(self.stamp) > delay:
            self.stamp = self.current_time
            return True
        else:
            return False
            

class block:
    def __init__(self):
        self.addr_map = {
            'type_1' : [[2,1],[2,2],[2,3],[3,3]],
            'type_2' : [[1,1],[1,2],[2,1],[2,2]],
            'type_3' : [[2,1],[2,2],[1,2],[1,3]],
            'type_4' : [[2,1],[2,2],[2,3],[2,4]],
            'type_5' : [[2,1],[2,2],[2,3],[1,3]],
            'type_6' : [[1,1],[1,2],[2,2],[2,3]],
            'type_7' : [[1,2],[2,2],[3,2],[2,1]]
        }

        return None

    def map(self, x, y , *address): #(예시)address = [[3,1],[1,3]]

        coordinate = []

        for addr in address:
            newX = addr[0] * 23 + x
            newY = addr[1] * 23 + y
            coordinate.append([newX, newY])

        return coordinate

    def test_rotate(self,x,y, str_type):
        addr_Map = self.addr_map[str_type]
        ADDR_map = self.rotate(addr_Map[0],addr_Map[1],addr_Map[2],addr_Map[3])
        coordinate = self.map(x,y, ADDR_map[0],ADDR_map[1],ADDR_map[2],ADDR_map[3])
        color = white

        info = {}

        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def rotate(self, *address): #(예시)address = [[3,1],[1,3]]
        rotate_map = {
            '1 1' : '1 3',
            '1 2' : '2 3',
            '1 3' : '3 3',
            '1 4' : '4 3',
            '2 1' : '1 2',
            '2 2' : '2 2',
            '2 3' : '3 2',
            '2 4' : '4 2',
            '3 1' : '1 1',
            '3 2' : '2 1',
            '3 3' : '3 1',
            '4 2' : '2 4'
        }

        lt = []
        for addr in address:
            addrX = addr[0]
            addrY = addr[1]

            addr_code_num = str(addrX) + ' ' + str(addrY)
            new_code_num = rotate_map[addr_code_num]

            split_new_code_num = new_code_num.split()
            sncnX = int(split_new_code_num[0])
            sncnY = int(split_new_code_num[1])

            addr_list = [sncnX,sncnY]
            lt.append(addr_list)

        return lt

    def rotate_type(self, str_type):
        if str_type == "type_2":
            return None
            
        addr_MAp = self.addr_map[str_type]

        ADDr_MaP = self.rotate(addr_MAp[0], addr_MAp[1], addr_MAp[2], addr_MAp[3])
        self.addr_map[str_type] = ADDr_MaP

        return None

    def draw(self, info):
        color = info['color']
        coor = info['coordinate']

        for cor in coor:
            coorX = cor[0]
            coorY = cor[1]

            draw_color_rect(color, coorX, coorY)

        return None

    def type_1(self, x,y):#L
        color = orange

        info = {}

        addr_map_type1 = self.addr_map['type_1']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def type_2(self, x,y):# O
        color = yellow

        info = {}

        addr_map_type1 = self.addr_map['type_2']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def type_3(self, x,y):#Z
        color = red

        info = {}
        
        addr_map_type1 = self.addr_map['type_3']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def type_4(self, x,y):# I
        color = light_blue

        info = {}
        
        addr_map_type1 = self.addr_map['type_4']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def type_5(self, x,y):# J
        color = blue

        info = {}
        
        addr_map_type1 = self.addr_map['type_5']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def type_6(self, x,y):# S
        color = green

        info = {}
        
        addr_map_type1 = self.addr_map['type_6']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

    def type_7(self, x,y): #T
        color = purple

        info = {}
        
        addr_map_type1 = self.addr_map['type_7']

        coordinate = self.map(x,y,addr_map_type1[0], addr_map_type1[1], addr_map_type1[2], addr_map_type1[3])
            
        info['color'] = color
        info['coordinate'] = coordinate

        return info

class stack:
    def stacked_block(self, stacked_block_list): #쌓인 블럭들을 그리는 함수
        for block in stacked_block_list:
            color = block['color']

            for coor in block['coordinate']:
                coorX = coor[0]
                coorY = coor[1]

                draw_color_rect(color, coorX, coorY)

        return None

    def check_stack(self, stacked_block_list):
        y_dict = {}
        

        for block in stacked_block_list: 
            coor = block['coordinate']

            for X_Y in coor:
                X = X_Y[0]
                Y = X_Y[1]
                stringY = str(Y)

                try:
                    K_E_Y = y_dict[stringY]

                except KeyError:
                    y_dict[stringY] = 0

                block_num = y_dict[stringY]
                y_dict[stringY] = block_num+1

        for key in y_dict:
            numY = int(key)

            if y_dict[key] == 10:
                return True, numY
            elif y_dict[key] < 10:
                continue
            
        return False, 'cookie'

    def clear_stack(self, stack_block_list, clear_y): #(예시) stack_block_list = [{'color' = blue, 'coordinate' = [[23, 234], [34, 234]]}, {'color' = mint, 'coordinate' = [23, 342], [87, 324]}]
        for block in stack_block_list:
            coor = block['coordinate']

            repeat_num = 0
            for X_Y in list(coor):
                Y = X_Y[1]

                if Y == clear_y:
                    del coor[repeat_num]
                    continue
                elif Y < clear_y:
                    new_Y = Y + 23
                    X_Y[1] = new_Y

                    repeat_num += 1
                    continue
                else:
                    repeat_num += 1
                    continue

        return stack_block_list

class movement:
    def fall_check(self, info):
        coor = info['coordinate']

        for cor in coor:
            if cor[1] >= 434:
                return True
            else:
                continue

        return False

    def colaps_check(self, info, stacked_block):
        coor = info['coordinate']

        for stk_blk in stacked_block:
            stacked_coor = stk_blk['coordinate']

            for stk in stacked_coor:
                stacked_coorX = stk[0]
                stacked_coorY = stk[1]

                for block in coor:
                    blockX = block[0]
                    blockY = block[1]

                    rct = Rect(blockX, blockY, 20, 20)
                    stack_rct = (stacked_coorX, stacked_coorY, 20, 20)

                    if rct.colliderect(stack_rct):
                        return True
                    else:
                        continue

        return False


size = [273, 479] #최소 사이즈 [273, 479]
screen = pygame.display.set_mode(size)
programIcon = pygame.image.load('ikon.png')

pygame.display.set_caption("Tetris")
pygame.display.set_icon(programIcon)

done = False
clock = pygame.time.Clock()

mt = fall_time()
blockY = 23
blockX = 115
stacked_block = []
Block = block()
move = movement()
stk = stack()
test_rotate = Block.test_rotate

score = 0

typ_dct = {
    1:Block.type_1,
    2:Block.type_2,
    3:Block.type_3,
    4:Block.type_4,
    5:Block.type_5,
    6:Block.type_6,
    7:Block.type_7
}

BlocK, str_type = random_type(typ_dct)
colaps_check = move.colaps_check

#메인 루프
while not done:
    xp = 100

    f = open("bestScore.txt", 'r')
    bestScore = int(f.read())
    f.close()

    clock_tick = clock.tick(120)

    for event in pygame.event.get(): #이벤트
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_DOWN]:
                if not stop_block_at_edge(BlocK(blockX, blockY)) and not colaps_check(BlocK(blockX, blockY +23), stacked_block):
                    delay = -1

            elif pressed[pygame.K_LEFT]:
                if not colaps_check(BlocK(blockX - 23, blockY), stacked_block) and not stop_block_at_edge(BlocK(blockX - 23, blockY)):
                    blockX -= 23

            elif pressed[pygame.K_RIGHT]:
                if not colaps_check(BlocK(blockX +23, blockY), stacked_block) and not stop_block_at_edge(BlocK(blockX +23, blockY)):
                    blockX += 23

            elif pressed[pygame.K_z]:
                if not colaps_check(test_rotate(blockX,blockY,str_type), stacked_block) and not stop_block_at_edge(test_rotate(blockX,blockY,str_type)):
                    Block.rotate_type(str_type)
            

        

    screen.fill(black)
    
    #테두리
    x = 0
    while x<254:
        draw_rect(x, 0)
        draw_rect(x, 459)

        x += 23
    
    y = 23
    while y<455:
        draw_rect(0, y)
        draw_rect(253, y)

        y += 23
    
    if mt.check(time.time()): #약 0.6초마다 내려가기
        if move.fall_check(BlocK(blockX, blockY)) or colaps_check(BlocK(blockX, blockY +23), stacked_block): #블럭위에 있거나 맵 끝에 있을때
            stacked_block.append(BlocK(blockX, blockY))
            Block.__init__()
            blockY = 23
            blockX = 115
            delay = 0.6

            BlocK, str_type = random_type(typ_dct)

        else: #blockY < 434 또는 블럭위에 있지 않을때
            blockY = blockY + 23
            
        BLOCK = BlocK(blockX, blockY)
        Block.draw(BLOCK)
    else:
        BLOCK = BlocK(blockX, blockY)
        Block.draw(BLOCK)

    stk.stacked_block(stacked_block)

    stack_clear, Y = stk.check_stack(stacked_block)

    if stack_clear:
        new_stacked_block = stk.clear_stack(stacked_block, Y)
        stacked_block = new_stacked_block

        score += xp

        if score >= bestScore:
            asdf = open("bestScore.txt", 'w')
            asdf.write(str(score))
            asdf.close()

    elif colaps_check(BlocK(blockX, blockY), stacked_block):
        done = True
        pygame.quit()

        stdout.write("\r" + '                           ')
        while True:
            stdout.write("\r" + 'game over')
            stdout.flush

    stdout.write("\r" + f"Score = {score}, bestScore = {bestScore}")
    stdout.flush

    pygame.display.flip()

pygame.quit()
