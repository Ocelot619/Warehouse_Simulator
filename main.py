import time
from robot import Robot
from order import Order
from racks import Racks
#from visualiser import print_map, clear_screen

class Warehouse:
    def __init__(self):
        self.order = Order()
        self.racks = Racks()
        self.created_orders = 0
        self.item = Racks.StockItem() #tutaj dodajemy __str__ z stock item podklasy
        self.robot = Robot(4,4, False) # x | y | is busy|
        self.robot.racks = self.racks
        
# main.py - w klasie Warehouse/Main
    def print_map(self, width=12, height=12):
        grid = [['.' for _ in range(width)] for _ in range(height)]
    
        for stock_item in self.racks.stock_list:
            x, y = stock_item.pos_x, stock_item.pos_y
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = stock_item.item_name[0].upper()
    
        rx, ry = self.robot.pos_x, self.robot.pos_y
        if 0 <= rx < width and 0 <= ry < height:
            grid[ry][rx] = 'B' if self.robot.is_busy else 'R'
    
        if self.robot.is_busy and self.robot.found_target:
            tx, ty = self.robot.target_x, self.robot.target_y
            if 0 <= tx < width and 0 <= ty < height:
                grid[ty][tx] = 'T'
    
        print("\n" + "-" * (width*2 + 1))
        print(f"Robot: ({rx},{ry}) {'busy' if self.robot.is_busy else 'free'} -> {self.robot.target_x},{self.robot.target_y}" if self.robot.is_busy else f"Robot: ({rx},{ry}) free")
        for row in reversed(grid):
            print('| ' + ' | '.join(row) + ' |')
        print("-" * (width*2 + 1))

# W pętli:
 # self. !
       

def main():
    warehouse = Warehouse()
    warehouse.racks.fill_stock()
    
    print(str(warehouse.item)) # drukujemy __str__ ze stock item

    while True:
       
        if  warehouse.order.order_count < warehouse.order.max_orders: #sprawdzamy czy mamy jakies ordery do wykonania
            warehouse.order.create_order(5 , "iphone 12") #order dodajemy nowy | quantity | Nazwa  
            warehouse.created_orders += 1
        
        warehouse.robot.taking_order(warehouse.order)    
        warehouse   .print_map() 
        warehouse.robot.update() #tworzymy u updatujemy | pozycja x,| pozycja y|
        time.sleep(2)
    
    
    
    
if __name__ == "__main__":
    main()
