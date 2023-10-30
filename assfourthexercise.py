import random

class Car:


    def __init__(self,reg_num,max_speed,curr_speed = 0,travelled_dist = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.travelled_dist = travelled_dist

    def print_deets(self):
        print(self.reg_num,self.max_speed,"km/hr",self.curr_speed,"km/hr",self.travelled_dist,"km",sep="|")

    def accelarate(self,change):
        if self.curr_speed+change>self.max_speed:
            self.curr_speed = self.max_speed
            print("Speed of ",self.reg_num,"is",self.curr_speed)
        elif self.curr_speed+change<0:
            print("Negative speed is not possible hence speed becomes 0")
            self.curr_speed=0
        else:
            self.curr_speed=self.curr_speed+change
            print("Speed of ",self.reg_num,"is",self.curr_speed)

    def drive(self,time,race_distance):
        if self.travelled_dist+(self.curr_speed*time)<=race_distance:
            self.travelled_dist=self.travelled_dist+(self.curr_speed*time)
            print(f"The car has now travelled {self.travelled_dist}")
        else:
            self.travelled_dist=race_distance

class Race:
    def __init__(self,name,race_distance):
        self.car_list=car_list = [Car('ABC-' + str(i + 1), random.randint(100, 200)) for i in range(10)]
        self.name=name
        self.race_distance=race_distance

    def hour_passes(self,car):
        car.accelarate(random.randint(-10, 15))
        car.drive(1, self.race_distance)
    def race_finished(self,car):
        if car.travelled_dist == self.race_distance:
            return False
    def print_status(self):
        print("Registration Number", "Maximum Speed", "Current Speed", "Travelled Distances", sep="|")
        for car in self.car_list:
            car.print_deets()
    def race_results(self):
        print("Registration Number","Maximum Speed", "Current Speed","Travelled Distances",sep="|")
        for car in self.car_list:
            if car.travelled_dist==self.race_distance:
                print("(----------Winner------------)")
            car.print_deets()
            if car.travelled_dist==self.race_distance:
                print("(----------Winner------------)")

gdd=Race("Grand Demolition Derby",800)
race_hours=0
vroom = True
while vroom == True:
    for car in gdd.car_list:
        gdd.hour_passes(car)
        if gdd.race_finished(car) == False:
            print(car.reg_num, "has finished first, they've won the race!!!")
            vroom = False
            break
    race_hours+=1
    if race_hours%10:
        gdd.print_status()
gdd.race_results()