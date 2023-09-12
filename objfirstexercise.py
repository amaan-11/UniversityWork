class Car:
    def __init__(self,reg_num,max_speed,curr_speed = 0,travelled_dist = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.travelled_dist = travelled_dist

    def print_deets(self):
        print("The registration number:",self.reg_num," \nThe maximum speed of the car =",self.max_speed,"km/hr\nThe current speed of the car =",self.curr_speed,"km/hr\nThe distance the car has travelled =",self.travelled_dist,"km")
car1 = Car("ABC-123", 142)
car1.print_deets()