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
        self.car_place = []
