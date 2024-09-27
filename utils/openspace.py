from utils.table import Table
from random import shuffle
class Openspace:

    def __init__(self):
        self.number_of_tables = 6
        self.tables=[]

        for i in range(self.number_of_tables):
            table= Table()
            self.tables.append(table)
        
    def organize(self,names):

        shuffle(names)       

        for name in names:           
            shuffle(self.tables)        
            assigned = False
            for table in self.tables:
                 if table.has_free_spot(): 
                     table.assign_seat(name) 
                     assigned=True
                 if assigned:
                     break
                     
                
                     
                    


    def display(self):
        for table_index, table in enumerate(self.tables):
            print(f"Table {table_index + 1}:")
            for seat_index, seat in enumerate(table.seats):
                occupant = seat.occupant if seat.occupant else "Empty"
                print(f"  Seat {seat_index + 1}: {occupant}")

           

    #def store(filename):