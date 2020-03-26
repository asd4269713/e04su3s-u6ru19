class Drink:            #宣告類別一定是大寫開頭 底下的函式開頭命名一定要小寫
    def __init__(self,new_name,new_price):
        self.__name=new_name
        self.__price=new_price
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        self.__price=new_price