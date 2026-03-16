

class Robot():
    def __init__(self, pos_x, pos_y, is_busy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_busy = is_busy
        self.name = "NRS 01" #niski robot skladujacy xDD 
        self.current_order = ()
        self.target_x = 0      
        self.target_y = 0             
        self.found_target = False  
             
    
    def update(self):
        #co 1 ticka printujemy pozycje
        print(f"ROBOT: {self.name} Current position: X: {self.pos_x} Y: {self.pos_y} Is Busy: {self.is_busy}")
        if self.is_busy:
            self.robot_move()
        
        
    def taking_order(self, order_manager):
        if not self.is_busy:
            self.order = order_manager.distrib_order()
            
            
            if self.order is not None:
                self.current_order = self.order
                self.is_busy = True
                print(f"ROBOT-ORDER:  {self.name} took order {self.order}")
            else:
                print(f"ROBOT-ORDER: No orders avalibe for {self.name}")
        else:
            print(f"ROBOT-ORDER: {self.name} is busy cannot take order")
            
    def robot_move(self):
        quantity, item_id, order_id = self.current_order
        print(f"ROBOT-MOVE: Jestem na pozycji x:{self.pos_x} y:{self.pos_y}")
        print(f"ROBOT-MOVE: Szukam: {item_id}")
        target_x,target_y = 0,0
        for stock_item in self.racks.stock_list:
            print(f"sprawdzam {stock_item.item_name}")
            if stock_item.item_name == item_id:
                target_x = stock_item.pos_x
                target_y = stock_item.pos_y
                print(f"ROBOT-MOVE: znaleziono {stock_item.item_name} na pozycji x:{target_x}y:{target_y}")
                
         
        if self.pos_x < target_x:  # am i on left?
            self.pos_x += 1         # go right
            print(f"  X{self.pos_x}")
        elif self.pos_x > target_x:  # am i on right?
            self.pos_x -= 1          # go left
            print(f" X{self.pos_x}")
        elif self.pos_y < target_y:  # am i on top?
            self.pos_y += 1          # go under
            print(f"  Y{self.pos_y}")
        elif self.pos_y > target_y:  # am i under?
            self.pos_y -= 1          # go up
            print(f"  Y{self.pos_y}")
        else:
            print(" jestem na miejscu")
            
        if self.pos_x == target_x and self.pos_y == target_y:
            print("ROBOT-MOVE: Im on position of item order")
            
        
        


    def set_position(self, pos_x, pos_y):
        #przyjmujemy x i y 
        self.pos_x = pos_x
        self.pos_y = pos_y