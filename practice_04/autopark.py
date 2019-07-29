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

    def car_place(self, car):
        global ID
        if not self.get_car() \
                and car.length < self.length \
                and car.width < self.width \
                and car.height < self.height \
                and car.weight < self.weight:

            self.car = car
            car.id = ID
            ID += 1
            return True
        else:
            return False


class Angar:
    def __init__(self, boxes):
        self.boxes = boxes

    def car_place(self, car):
        for box in self.boxes:
            if box.get_car():
                continue
            elif box.car_place(car):
                return True
            else:
                continue
        else:
            return False

    def get_car(self, id):
        for b in self.boxes:
            car = b.get_car()
            if car and car.id == id:
                return car
            else:
                continue
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
                continue
        else:
            return False

    def get_car(self, id):
        for ang in self.angars:
            car = ang.get_car(id)
            if car:
                return car
            else:
                continue
        else:
            return None


car_lst = [Car(randint(2, 4), randint(2, 4), randint(2, 4), randint(2, 4)) for _ in range(15)]
box_ls1 = [Box(randint(3, 5), randint(3, 5), randint(3, 5), randint(3, 5)) for _ in range(5)]
box_ls2 = [Box(randint(3, 5), randint(3, 5), randint(3, 5), randint(3, 5)) for _ in range(5)]
box_ls3 = [Box(randint(3, 5), randint(3, 5), randint(3, 5), randint(3, 5)) for _ in range(5)]

ang1 = Angar(box_ls1)
ang2 = Angar(box_ls2)
ang3 = Angar(box_ls3)

autopark = AutoParking([ang1, ang2, ang3])

id_list = []
for i in car_lst:
    if autopark.car_place(i):
        id_list.append(i.id)
print(id_list)
print('=' * 50)
print(len(id_list))

car_return_list = []
for id in id_list:
    car = autopark.get_car(id)
    if car:
        car_return_list.append(car)

print(car_return_list)
print(len(car_return_list))
