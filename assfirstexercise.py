class Elevator:

    def __init__(self,bottom,top,current):
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



#main
elevator=Elevator(0,10,0)
target=int(input("What floor would you like to go to?"))
elevator.go_to_floor(target