class Room:
    def __init__(self, long, width, num_windows):
        self.long = long
        self.width = width
        self.num_windows = num_windows

    def get_area(self):
        return self.long * self.width

    def get_num_windows(self):
        return self.num_windows


class Apartment:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_area_rooms(self):
        sum_sq = 0
        for r in self.rooms:
            sum_sq += r.get_area()
        return sum_sq

    def get_num_windows_rooms(self):
        sum_winds = 0
        for r in self.rooms:
            sum_winds += r.get_num_windows()
        return sum_winds


r1 = Room(10, 20, 2)
r2 = Room(5, 4, 1)
r3 = Room(10, 4, 3)

ap = Apartment()

ap.add_room(r1)
ap.add_room(r2)
ap.add_room(r3)

print(ap.get_area_rooms())
print(ap.get_num_windows_rooms())
