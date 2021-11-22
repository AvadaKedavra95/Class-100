class Car(object):
    def __init__(self,color,company,seats,number,state):
        self.color=color
        self.company=company
        self.seats=seats
        self.number=number
        self.state=state

    def start(self):
        print('started')
    
    def carcando(self):
        print('my car can fly')
    
    def speed(self):
        print("the max speed of my car is 5000 miles/hour")
        

car1=Car("red","audi",8,5213,"delhi")
print(car1.color)
print(car1.company)
print(car1.seats)
print(car1.number)
print(car1.state)
car1.speed()
car1.carcando()
car1.start()