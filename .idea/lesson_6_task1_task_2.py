class Car:
    is_busy=False
    def __init__ (self,color :str ,count_passenger_seats :int ,is_baby_seat :bool):
        self.color=color
        self.count_passenger_seats=count_passenger_seats
        self.is_baby_seat=is_baby_seat
        self.is_busy=False

    def __str__(self):
        return f"{self.color,self.count_passenger_seats,self.is_baby_seat,self.is_busy}"

car1 = Car (color="Geen",count_passenger_seats=5,is_baby_seat=False)
car2 = Car (color="Red",count_passenger_seats=4,is_baby_seat=True)
#print(car1)
#print(car2)

class Taxi(Car):
    def __init__(self,*cars):
        self.cars=cars[:]

    def __str__(self):
        return f"{self.cars}"
    def find_car(self,count_passenger_seats, is_baby_seat):
        for car in self.cars:
            if car.is_busy==False and car.count_passenger_seats==count_passenger_seats and car.is_baby_seat==is_baby_seat:
                car.is_busy = True
                print(car)
            else:
                print("None")








cars=[]
cars.append(car1)
cars.append(car2)

taxi_cars=Taxi(*cars)
taxi_cars.find_car(4,True)



