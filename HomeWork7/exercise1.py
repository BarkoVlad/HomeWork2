class Car:
    def __init__(self, brand, model, yearofissue, speed):
        self.brand = brand
        self.model = model
        self.yearofissue = yearofissue
        self.speed = speed
    def speedhigh(self):
        self.speed += 5
    def speedsmall(self):
        self.speed -= 5
    def speedstop(self):
        self.speed = 0
    def speedback(self):
        self.speed = self.speed * -1
    def printspeed(self):
        print(self.speed)
car = Car('BMW','X7',2021, 120)
car.speedhigh()
car.printspeed()
car.speedsmall()
car.printspeed()
car.speedback()
car.printspeed()
car.speedstop()
car.printspeed()
print(car.brand)
print(car.model)
print(car.yearofissue)
print(car.speed)
