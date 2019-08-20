import numpy as np
from PIL import Image
import cv2
SIZE=25
HM_EPISODES=10000

d={1:(255, 0, 0),#blue player
   2:(0, 255, 0), #green food
   3:(0, 0, 255 )}#reed enemy
PLAYER_N=1
FOOD_N=2
ROAD_N=3
class simu:
    def __init__(self):
        
        self.x=0#np.random.randint(0, SIZE)  
        self.y=12#np.random.randint(0, SIZE)
        
    def __str__(self):
        return f"Blob ({self.x}, {self.y})"
    def __sub__(self, other):
        return (self.x-other.x, self.y-other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def action(self, choice):
        '''
        Gives us 9 total movement options. (0,1,2,3,4,5,6,7,8)
        '''
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)

        elif choice == 4:
            self.move(x=1, y=0)
        elif choice == 5:
            self.move(x=-1, y=0)

        elif choice == 6:
            self.move(x=0, y=1)
        elif choice == 7:
            self.move(x=0, y=-1)

        elif choice == 8:
            self.move(x=0, y=0)

    def move(self, x=False, y=False):
        if not x:
            self.x += np.random.randint(-1, 2)
        else:
            self.x += x
        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y    
        if self.x<0:
            self.x=0
        elif self.x>SIZE-1:
            self.x=SIZE-1
        if self.y<0:
            self.y=0
        elif self.y>SIZE-1:
            self.y=SIZE-1   
       

show_every=15

for i in range(150):
    player=simu()
##    food=simu()
    if i%show_every==0:
        print(f"on  {i} epoch player's position {player}")
        
        show=True
    else:
        show=False
    for j in range(200):
        action=np.random.randint(0, 9)
        player.action(action)
        
        if show:
        
            env=np.zeros((SIZE, SIZE, 3), dtype=np.uint8)       
            food=env[0][12:13]
            food=d[FOOD_N]
            env[5][5:24]=d[ROAD_N]
            env[12][2:12]=d[ROAD_N]
            env[20][7:17]=d[ROAD_N]
            
            env[player.x][player.y]=d[PLAYER_N]
##            if player==food:
##                print("made it")    
            img= Image.fromarray(env, "RGB")
            img=img.resize((400, 400))
            cv2.imshow("", np.array(img))
            cv2.waitKey(1)
            
