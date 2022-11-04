class Car:
    def __init__(self, brand, model, yearofissue, speed):
        self.brand = brand
        self.model = model
        self.yearofissue = yearofissue
        self.speed = speed
    def speedhigh(self):
        print('Увеличение скорости на 5 = ', self.speed + 5)
    def speedsmall(self):
        print('Уменьшение скорости на 5 = ', self.speed - 5)
    def speedstop(self):
        print('Движение задним ходом', self.speed == 0)
car = Car('BMW','X7',2021, 120)
car.speedhigh()
car.speedsmall()
car.speedstop()
print(car.brand)
print(car.model)
print(car.yearofissue)
print(car.speed)