class Seat:
  #This is a seat

  def __init__(self):
    self.free = True
    self.occupant = ""

  def set_occupant(self,name):
    self.free = False
    self.occupant = name

  def remove_occupant(self):
    self.free = True
    self.occupant = ""







names = list[range(0,25)]
list_seats = []
for name in names:
    seat = Seat()
    seat.set_occupant(name)
    list_seats.append(seat)   
        



             

class Table:

    def __init__(self, capacity:int):
        self.capacity =  4
        self.seats = []
        for i in range(self.capacity):
           seat = Seat()
           self.seats.append(seat)


    def has_free_spot(self):
        for i in self.seats:
           if i.free == True:
              return True
              break
        


    def assign_seat(self, name):
       for i in self.seats:
          i.set_occupant(name)
       


    def left_capacity():
       



    

        


