#!/usr/bin/env python3

class CashRegister:
    def __init__(self,discount=0):
        self.discount = discount
        self.items = []
        self.previous = []
        self.total = 0
    
    def add_item(self,item,price,quantity=1):
        product = {"item":item, "price":price, "quantity":quantity}
        self.total += product["price"] * product["quantity"]
        for _ in range(quantity):
            self.items.append(product["item"])
        self.previous.append(product)
    
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.total -= (
                self.previous[-1]["price"] * self.previous[-1]["quantity"]
            )
            

        
