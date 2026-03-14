import time
from robot import Robot
from order import Order


def main():
    robot = Robot(1,1)
    order = Order()

    while True:
        robot.update() #tworzymy u updatujemy | pozycja x,| pozycja y|
        order.create_order(5 , "iphone 12") #order dodajemy nowy | quantity | Nazwa  
        time.sleep(2)
    
    
    
    
    
main()