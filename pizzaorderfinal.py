import csv
import datetime

class Pizza:
    def __init__(self):
        self.description = "Bir pizza"
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Classic(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza"
        self.cost = 15.0

class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita pizza"
        self.cost = 20.0

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "TurkPizza pizza"
        self.cost = 22.0
        
class PlainPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Plain pizza"
        self.cost = 25.0

class Decorator:
    def __init__(self, pizza):
        self.component = pizza

    def get_description(self):
        return self.component.get_description() + ", " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost

class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "zeytin"
        self.cost = 2.0


class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "mantar"
        self.cost = 3.0


class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "keçi peyniri"
        self.cost = 2.5

class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "sucuk"
        self.cost = 2.0


class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "soğan"
        self.cost = 3.0


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "mısır"
        self.cost = 2.5

def main():
    with open('Menu.txt','r') as menu:
        menutext = menu.read()
    print (menutext)
    choose_pizza = True
    choose_decorator = True
    print('Please choose a pizza from menu and enter the number:')
    while(choose_pizza):
        pizza_order = input()
        if pizza_order == "1":
            pizza = Classic()
            choose_pizza=False
        elif pizza_order == "2":
            pizza = Margherita()
            choose_pizza=False
        elif pizza_order == "3":
            pizza = TurkPizza()
            choose_pizza=False
        elif pizza_order == "4":
            pizza = PlainPizza()
            choose_pizza=False
        else:
            print("Please enter a valid order!")
    print('Please choose a sauce as decorator from menu and enter the number:')
    while (choose_decorator):
        pizza_order = input()
        if pizza_order == "11":
            decorator = Olives(pizza)
            choose_decorator=False
        elif pizza_order == "12":
            decorator = Mushrooms(pizza)
            choose_decorator=False
        elif pizza_order == "13":
            decorator = GoatCheese(pizza)
            choose_decorator=False
        elif pizza_order == "14":
            decorator = Meat(pizza)
            choose_decorator=False
        elif pizza_order == "15":
            decorator = Onions(pizza)
            choose_decorator=False
        elif pizza_order == "16":
            decorator = Corn(pizza)
            choose_decorator=False
        else:
            print("Please enter a valid order!")
    print(decorator.get_description())
    print(decorator.get_cost(),"TL")
    print('Please enter your name:')
    name = input()
    print('Please enter your ID number:')
    id_number = input()
    print('Please enter your credit card number:')
    credit_card = input()
    print('Please enter your credit card password:')
    password = input()
    order = [name,id_number,credit_card,password,decorator.get_description(),datetime.datetime.now()]
    try:
      with open("Orders_Database.csv", 'r') as f:
          pass 
    except FileNotFoundError:
      with open("Orders_Database.csv", 'w', newline='') as f:
          writer = csv.writer(f)
          writer.writerow(['name', 'ID', 'CardID', 'CardPsswrd', 'Order', 'date']) 

    with open("Orders_Database.csv", 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(order) 
        
main()
