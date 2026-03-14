import time
from robot import Robot


def main():
    robot = Robot(1,1)

    while True:
        robot.update() #robot.update pozycja x, pozycja y
        time.sleep(1)
    
    
    
    
    
main()