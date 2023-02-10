import random
from beverages import *

class CoffeeMachine:
    
    def __init__(self):
        self.counter = 10
        self.broken = 0
       
    class EmptyCup(HotBeverage):
        price = 0.90
        name = "empty cup"
        def description(self):
            return ("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __str__(self, message = "This coffee machine has to be repaired."):
            raise Exception (message)

    def repair(self):
        self.counter = 10
        self.broken = 0

    def serve(self, drink):
        if self.counter == 0: 
            try:
                print(CoffeeMachine.BrokenMachineException())
            except Exception as e:
                print (e)

        if self.counter > 0:
            self.counter -=1
            i = [1, 2]
            select = random.choice(i)
            if select == 1:
                return(drink())
            else:
                return(self.EmptyCup())
        else:
           return


if __name__ == "__main__":
    machine = CoffeeMachine()
    options = [Cappucino, Tea, Coffee,Chocolate, HotBeverage]

    counter = 1
    for i in range(23):
        try:
            result = machine.serve(random.choice(options))
            if result != None:
                print(result, counter)
        except Exception as e:
            print(e)
        if (counter % 11 == 0):
            machine.repair()
            print("Repairing Machine")
        counter +=1
