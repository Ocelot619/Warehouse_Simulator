

class Robot():
    def __init__(self, pos_x, pos_y, is_busy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_busy = is_busy
        self.name = "NRS 01" #niski robot skladujacy xDD 
        self.current_order = ()        
    
    def update(self):
        #co 1 ticka printujemy pozycje
        print(f"{self.name} Current position: X: {self.pos_x} Y: {self.pos_y} Is Busy: {self.is_busy}")
        
        
    def taking_order(self):
        if self.is_busy == False:
            
            
        
        


    def set_position(self, pos_x, pos_y):
        #przyjmujemy x i y 
        self.pos_x = pos_x
        self.pos_y = pos_y