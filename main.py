import time
from robot import Robot
from order import Order

class Warehouse:
    def __init__(self):
        self.robot = Robot(1,1)
        self.order = Order()
        self.created_orders = 0


def main():
    warehouse = Warehouse()
    

    while True:
       
        if  warehouse.order.order_count < warehouse.order.max_orders: #sprawdzamy czy mamy jakies ordery do wykonania
            warehouse.order.create_order(5 , "iphone 12") #order dodajemy nowy | quantity | Nazwa  
            warehouse.created_orders += 1
            
        warehouse.robot.update() #tworzymy u updatujemy | pozycja x,| pozycja y|
        time.sleep(2)
    
    
    
    
if __name__ == "__main__":
    main()
