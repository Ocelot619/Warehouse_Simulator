class Order:
    def __init__(self):
        #self.__quantity = quantity
        #self.__item_id = item_id
        print("uruchamianie obiektu order")
        
    
    def create_order(self, quantity, item_id):
        self.__quantity = quantity
        self.__item_id = item_id
        print("uruchamianie | funkcji |  obiektu order |create order")
        print(f"Aktualne zamowienie: ilosc {self.__quantity} item id: {self.__item_id}")
        
        