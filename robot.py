class Robot():
    def __init__(self, pos_x, pos_y ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = "NRS 01" #niski robot skladujacy xDD 
        
    def update(self):
        #co 1 ticka printujemy pozycje
        print(f"{self.name} Current position: X: {self.pos_x} Y: {self.pos_y} ")
        


    def set_position(self, pos_x, pos_y):
        #przyjmujemy x i y 
        self.pos_x = pos_x
        self.pos_y = pos_y