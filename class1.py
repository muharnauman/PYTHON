class car():
    def __init__(self,name,make,model,year):

        self.name=name
        self. make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def description(self):
        print("   ",self.name,"       ",self.make,"     ",self.model,"          ",self.year)  
    def read_odometer(self):
        print("the reading od odometer is",self.odometer_reading)
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("you can't roll back an odometer !")
    def increase(self,miles):
        self.odometer_reading+=miles
class eletricCar(car)  :
    def __init__(self, name, make, model, year):
        super().__init__(name, make, model, year)
        self.battery_s=batry
        
    def showcars(self)    :
        print(self.name,"  ",self.make,"  ",self.model,"  ",self.year)
class batry():
    def bettery_p (self,battery_s=70):
        self.battery_s=battery_s
    def battery_d(self):
         print("this car has a ",self.battery_s,"-KWH BATTERY")      
mycar=eletricCar("tesla","audi","f17",1200)
mycar.description() 
newd=batry(30)
newd.battery_d()
