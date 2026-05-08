#!/usr/bin/env python3

class CashRegister:
  #this wouldnt run without initializing like this
  def __init__(self, discount=0, total=0.0): 
      self.total=total 
      self.items=[]
      self.previous_transactions=[]
      self.discount=discount
  @property
  def discount(self):
     return self._discount
  @discount.setter
  def discount(self,val):
     if type(val) is int and 0<=val<=100: 
        self._discount=val
     else:
      raise ValueError("Not valid discount")
    
  def add_item(self, item,price,quantity=1):
     if quantity <= 0: 
      raise ValueError("Quantity must be greater than or equal to 0.")
     self.total+=price*quantity
     for q in range (0,quantity):
      self.items.append(item) 
     self.previous_transactions.append([item,price,quantity])


     
  def apply_discount(self):
    if self.discount<=0:
      print("There is no discount to apply.")
      return  
    self.total= self.total*(1- self.discount/100) 
    print(f"After the discount, the total comes to ${int(self.total)}.")
   
     
  def void_last_transaction(self):

    #finally down here. yeah thisll be done soon:tm:, alright
    if self.previous_transactions:
      #removes last item
      popped=self.previous_transactions.pop()
      if self.previous_transactions: #checks if the thing is full after and resets total [basic]. 
        self.total-=popped[1]*popped[2] #this checks the transaction 
      else: #if list is empty, default to 0.0 and prints for test reasons.
        self.total=0.0 
    else: print("There is no transactions to void") #if all breaks says nothings to remove.
#theres no issues according to the tests, i doubled up because itll freakout otherwise


    
#if __name__ == "__main__": #manual testing
#    cR=CashRegister()
#    cR.add_item("eggs",1.99,20)
#    cR.add_item("tomato", 1.76,1)
#    cR.add_item("tomato", 1.76,9)
#    print(f"{cR.previous_transactions}, {cR.total:.2f}") #not really, but im pleased this is done with 
#    cR.void_last_transaction()
#    print(f"{cR.previous_transactions}, {cR.total:.2f}")#only tweaked formatting.

   ##cR.void_last_transaction()

