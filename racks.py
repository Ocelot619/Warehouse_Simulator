class Racks():
    class StockItem:
        def __init__(self):
            self.item_name = "iphone 12"
            self.pos_x = 5
            self.pos_y = 3
            self.quantity = 5 
            
            
        def __str__(self):
            return f"Racks item: {self.item_name} pos_x: {self.pos_x} pos_y: {self.pos_y}"    
        
    def __init__(self):
        self.stock_list = []
        
    def fill_stock(self):
        #tworzymy przedmiot i dodajemy do listy
        item = self.StockItem()
        self.stock_list.append(item)
        print(f"added to stock {item}")
        
        