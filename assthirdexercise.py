class Elevator:

    def __init__(self,name,bottom,top,current):
        self.name=name
        self.bottom=bottom
        self.top=top
        self.current=current


    def floor_up(self):
        self.current=self.current+1
        print(f"Floor No. {self.current}")

    def floor_down(self):
        self.current=self.current-1
        print(f"Floor No. {self.current}")

    def go_to_floor(self,target):
        print(f"Floor No. {self.current}")
        if target>self.current:
            for i in range(target-self.current):
                self.floor_up()
        elif target<self.current:
            for i in range(self.current-target):
                self.floor_up()
        print("Destination Floor reached, Please exit")


class Building:

    def __init__(self,bottom,top,num_elevators):
        self.bottom=bottom
        self.top=top
        self.num_elevators=num_elevators
        self.elevators= [Elevator('Elevator' + str(i + 1),self.bottom,self.top,0) for i in range(self.num_elevators)]
    def run_elevator(self,elevator_num,target):
        self.elevators[elevator_num-1].go_to_floor(target)
    def firealarm(self):
        print("PLEASE EVACUATE THE BUILDING I REPEAT PLEASE EVACUATE THE BUILDING")
        for i in range(self.num_elevators):
            self.elevators[i].go_to_floor(0)

#main
empirestate=Building(0,300,5)
elevator_num=int(input("Enter the elevator number you want to use."))
target=int(input("Enter the floor you'd like to go to."))
empirestate.run_elevator(elevator_num,target)
empirestate.firealarm()
