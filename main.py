import time
from robot import Robot
from order import Order
from racks import Racks

class Warehouse:
    def __init__(self):
        self.robot = Robot(4,4)
        self.order = Order()
        self.racks = Racks()
        self.created_orders = 0
        self.item = Racks.StockItem() #tutaj dodajemy __str__ z stock item podklasy

def main():
    warehouse = Warehouse()
    warehouse.racks.fill_stock()
    print(str(warehouse.item)) # drukujemy __str__ ze stock item
    
    
    

    while True:
       
        if  warehouse.order.order_count < warehouse.order.max_orders: #sprawdzamy czy mamy jakies ordery do wykonania
            warehouse.order.create_order(5 , "iphone 12") #order dodajemy nowy | quantity | Nazwa  
            warehouse.created_orders += 1
            
        warehouse.robot.update() #tworzymy u updatujemy | pozycja x,| pozycja y|
        time.sleep(2)
    
    
    
    
if __name__ == "__main__":
    main()
