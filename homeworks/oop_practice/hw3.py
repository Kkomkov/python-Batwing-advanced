from abc import ABC, abstractmethod  
import random

class Person():
    def __init__(self, name, age, money_amount, have_home):
        self._name = name
        self._age = age
        self._money = money_amount
        self._have_a_home = have_home
    
    def name(self)->str:
        return self._name
    
    def get_age(self): 
        return self.age
    
    def get_money_amount(self): 
        return self._money
    
    def is_home_owner(self):
        return self._have_a_home
    
    def make_money(self, new_money):
        self._money += new_money
        print (f"{self._name} gain {new_money}")
    
    def buy_house(self, home, agent, new_price):
        
        if self._money >= new_price:
            self.withdraw_money(new_price)
            self._have_a_home = agent.sell_house(home, self, new_price)           
        else:
            print ("Fail, you have no money for this house.")
        
        
    def withdraw_money(self, amount):
        self._money -= amount
        
    def info(self):
        return f"Name:{self._name}, money:{self._money}, have a home:{self._have_a_home}"

    
class House():
    def __init__(self, area:int, cost:int,address:str):
        self._size = area
        self._cost = cost
        self._address = address
        
    def size(self)->int: return self._size
    def cost(self)->int: return self._cost
    def address(self)->str: return self._address
   
    def __str__(self) :
        return f"size :{self._size}, cost:{self._cost}, adress:{self._address}"
    
class EstateAgentMeta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            new_instance = super().__call__(*args, **kwds)
            cls._instances[cls] = new_instance
        return cls._instances[cls]

class EstateAgent(metaclass = EstateAgentMeta):
    def __init__(self, name:str, houses:list[House] , discounts:int, scam_chance:int):
        self._name = name
        self._houses = houses
        self._discounts = discounts
        self._scam_chance = scam_chance
        
    def __str__(self) -> str:
        return f"Name: {self._name}, scam chance: {self._scam_chance}%"
    
    def houses(self):return self._houses
    def houses_by_size(self, size):
        result = [] 
        for house in self._houses:
            if house.size() <= size:
                result.append(house)
                
        return result

    def name(self):return self._name
    
    def discount(self, client_name):
        return 0
    
    def _make_trick(self) ->bool:
        n = random.randrange(0,99)
        result = (self._scam_chance > n )
        return result
        
    def sell_house(self, house, client, new_price):
        result = not(self._make_trick())
        if result :
            print(f"Congratulation!, {client.name()} you bough a house for {new_price}")
        else:
            print(f"Ha ha ha! I trick you, {client.name()}")
            
        return result
    

houses = [
    House(42, 13000,"street 1"), 
    House(40, 10000,"street 2"), 
    House(200, 40000,"street 3")
]

kim = Person("Kim", 25, 9000, False)
dorothy = Person("Dorothy", 40, 100000, False)

realtor = EstateAgent("Realtor 1", houses, {"Kim":300,"Dorothy":1000}, 10)
realtor2= EstateAgent() 
print(realtor2)

discount = realtor.discount(kim)

while  kim.is_home_owner() == False:
    print (kim.info())
    for home in realtor.houses_by_size(42):
        home_new_price = (home.cost()-discount)
        if kim.get_money_amount() > home_new_price:
            kim.buy_house(home, realtor, home_new_price)
        else:
            print(f"{kim.name()}, You need more money to buy a house with address {home.address()}")
            
    kim.make_money(1000)
    