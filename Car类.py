class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model= model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name
	
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) +" miles on it.")
	
	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading = mileage
		else :
			print("You can't roll back an odometer!")
	
	def increment_odometer(self,miles):
		if miles>=0:
			self.odometer_reading += miles
		else :
			print("You can't roll back an odometer!")
my_new_car = Car('Audi','a4',2016)
print(my_new_car.get_descriptive_name())
raw_mileage = input("How many miles has your car on ?")
raw_mileage = int(raw_mileage)
my_new_car.update_odometer(raw_mileage)
#my_new_car.read_odometer()
increase_miles = int(input("How many miles have been added to your car?"))
my_new_car.increment_odometer(increase_miles)
my_new_car.read_odometer()
update_mileage = int(input("You can update your car's mileage by input it: "))
my_new_car.update_odometer(update_mileage)
my_new_car.read_odometer()
