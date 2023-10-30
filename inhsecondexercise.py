import random
class Car:

    def __init__(self,reg_num,max_speed,curr_speed = 0,travelled_dist = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.travelled_dist = travelled_dist

    def print_deets(self):
        print(self.reg_num,self.max_speed,"km/hr",self.curr_speed,"km/hr",self.travelled_dist,"km",sep="|")

    def accelerate(self,change):
        if self.curr_speed+change>self.max_speed:
            self.curr_speed = self.max_speed
            print("The current speed of ",self.reg_num,"is",self.curr_speed)
        elif self.curr_speed+change<0:
            print("Negative speed is not possible hence speed becomes 0")
            self.curr_speed=0
        else:
            self.curr_speed=self.curr_speed+change
            print("Speed of ",self.reg_num,"is",self.curr_speed)

    def drive(self,time):
        if self.travelled_dist+(self.curr_speed*time)<=10000:
            self.travelled_dist=self.travelled_dist+(self.curr_speed*time)
            print(f"The car has now travelled {self.travelled_dist}")

class Electricar(Car):
    def __init__(self,batterycapacity,reg_num,max_speed,curr_speed=0,travelled_dist=0):
        super().__init__(reg_num,max_speed,curr_speed,travelled_dist)
        self.batterycapacity=batterycapacity



class Gasolinecar(Car):
    def __init__(self,tankcapacity,reg_num,max_speed,curr_speed = 0,travelled_dist = 0):
        super().__init__(reg_num,max_speed,curr_speed,travelled_dist)
        self.tankcapacity=tankcapacity
cars=[]
cars.append(Electricar("52.5 kw/h","ABC-15",180))
cars.append(Gasolinecar("32.3 l","ACD-15", 165))
hours=0
while hours<=3:
    for car in cars:
        car.accelerate(random.randint(0,15))
        car.drive(1)
    hours+=1
print("Registration Number","Maximum Speed", "Current Speed","Travelled Distance",sep="|")
for car in cars:
    car.print_deets()
