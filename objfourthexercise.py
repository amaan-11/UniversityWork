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

assign=[Car('ABC-'+str(i+1),random.randint(100,200)) for i in range(10)]
while True:
    for car in assign:
        if car.travelled_dist == 10000:
            print(car.reg_num,"has finished first, they've won the race!!!")
            break

        car.accelarate(random.randint(-10,15))
        car.drive(1)
    if car.travelled_dist == 10000:
        break
print("Registration Number","Maximum Speed", "Current Speed","Travelled Distances",sep="|")
for car in assign:
    car.print_deets()
