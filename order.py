class Order:
    def __init__(self):
        self.__order_list = []
        self.order_count = 0
        self.max_orders = 2
        #print("uruchamianie obiektu order")
        
    
    def create_order(self, quantity, item_id):
        self.__quantity = quantity
        self.__item_id = item_id
        self.order_count += 1
        self.order_id = f"Order 00{self.order_count}"
       # print("uruchamianie | funkcji |  obiektu order |create order")
        print(f"Aktualnie generowane zamowienie: ilosc {self.__quantity} item id: {self.__item_id} order id: {self.order_id}")
        current_order = (self.__quantity, self.__item_id, self.order_id)
        self.__order_list.append(current_order)
        