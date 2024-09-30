class Seat:
  #This is a Seat

  def __init__(self):
    self.free = True
    self.occupant = ""

  def set_occupant(self,name):
    if self.free: #to check whether the seat is free
       self.occupant = name
       self.free = False
       
       
  def remove_occupant(self):    
    name =self.occupant
    self.free = True
    self.occupant = ""
    return name


            

class Table:

    def __init__(self):
        self.capacity =  4
        self.seats = []

        for i in range(self.capacity):
           seat = Seat()
           self.seats.append(seat)


    def has_free_spot(self):
        
        for seat in self.seats:
           if seat.free:
              return True
        return False
           
        
        

    def assign_seat(self, name):
       for seat in self.seats:
          if seat.free:
             seat.set_occupant(name)
             break
            
       


    def left_capacity(self):
       count=0       
       for seat in self.seats:
          if seat.free:
             count += 1
            
       return count
    
    
       
    
      
        
             
       



    

        


