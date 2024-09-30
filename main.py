from utils.openspace import Openspace
from utils.table import Table
import csv

with open("utils/new_colleagues.csv", newline="") as csv_file:
    contents = csv.reader(csv_file, delimiter=" ", quotechar="|")
    names = []
    for row in contents:
        names.append(row)
    print(names)


openSpace = Openspace()

openSpace.organize(names)

openSpace.display()

table = Table()

table.left_capacity()