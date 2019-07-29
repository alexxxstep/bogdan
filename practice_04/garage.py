from random import randint

ID = 100

class Car:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self._id = ''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


class Box(Car):
    def __init__(self, length, width, height, weight):
        super().__init__(length, width, height, weight)
		self.car = None 
	 
    def get_car(self):
        return self.car
    
    def car_place(self, new_car):
		global ID
		if self.get_car():			
			return False
		elif new_car.length < self.length and new_car.width < self.width and new_car.height < self.height and new_car.weight < self.weight:
			 
			self._car = new_car
			new_car.id = ID
			ID += 1
			return True
		else:
			 
			return False	
		
		
class Angar:
	def __init__(self, boxes):
		self.boxes = boxes
		
	def car_place(self, car):		
		for box in self.boxes:
			if not box.car_place(car):
				continue
			return box.car_place(car)
		else:
			return False
			
	def get_car(self, id):		
		for b in boxes:
			car = b.get_car()
			if car and car.id == id:
				car = self.car
				b.car = None
				return b.car
		else:
			return None
			
class AutoParking:
	def __init__(self, angars):
		self.angars = angars
		
	def car_place(self, car):
		for ang in self.angars:
			if ang.car_place(car):
				return True
		else:
			return False

	
	def get_car(self,id):
		for ang in self.angars:
			car = ang.get_car(id)
			if car:
				return car
		else:
			return None
				
			
car_lst = [Car(randint(1,3), randint(1,3), randint(1,3),randint(1,3)) for _ in range(10)]	
box_ls1 = [Box(randint(3,5), randint(3,5), randint(3,5),randint(3,5)) for _ in range(3)]	
box_ls2 = [Box(randint(3,5), randint(3,5), randint(3,5),randint(3,5)) for _ in range(4)]
box_ls3 = [Box(randint(3,5), randint(3,5), randint(3,5),randint(3,5)) for _ in range(2)]

ang1 = Angar(box_ls1)
ang2 = Angar(box_ls2)
ang3 = Angar(box_ls3)

autoparking = AutoParking([ang1,ang2,ang3])

for i in car_lst:	
	if autoparking.car_place(i):
		c = car_lst.pop(i)
		

		
		
