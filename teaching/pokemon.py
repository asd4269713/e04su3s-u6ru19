class Pokemon:
    def __init__(self,new_name,new_weight,new_height,new_food,new_cp):
        self.__name=new_name
        self.__weight=new_weight
        self.__height=new_height
        self.__food=new_food
        self.__cp=new_cp
    def set_name(self,new_name):
        self.__name=new_name
    def get_name(self):
        return self.__name
    def set_weight(self,new_weight):
        self.__weight=new_weight
    def get_weight(self):
        return self.__weight
    def set_height(self,new_height):
        self.__height=new_height
    def get_height(self):
        return self.__height
    def set_food(self,new_food):
        self.__food=new_food
    def get_food(self):
        return self.__food
    def set_cp(self,new_cp):
        self.__cp=new_cp
    def get_cp(self):
        return self.__cp
    def eat(self,new_food):
        print(f"The pokemon is eating {new_food}")
    def make_voice(self):
        print("The pokemon wow wow wow!")
class pikachu(Pokemon):
    def __init__(self,new_name,new_weight,new_height,new_food,new_cp):
        super().__init__(new_name,new_weight,new_height,new_food,new_cp)

    def eat(self):
        print(f"{self.get_name} is eating {self.get_food}.pika")

    def make_voice(self):
        print(f"{self.get_name} pika pika chu!")

class Squirtle(Pokemon):
    def __init__(self,new_name,new_weight,new_height,new_food,new_cp):
        super().__init__(new_name, new_weight, new_height, new_food, new_cp)

    def eat(self):
        print(f"{self.get_name} is eating {self.get_food}.jenny jenny")

    def make_voice(self):
        print(f"{self.get_name} jenny jenny!")
a1=Pokemon('DOG','60','170','fish','160')
a2=pikachu('Cat','69','160','meat','50')
a3=Squirtle('jenny','100','200','turtle','300')
ls=[a1, a2, a3]
for item in ls:
    item.make_voice()

