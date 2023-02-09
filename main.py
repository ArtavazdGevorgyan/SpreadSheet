from cell import Cell
from spreadsheet import Spreadsheet


sp = Spreadsheet(2,3)
for i in range(2):
    for j in range(3):
        sp.setCellAt(i,j,Cell(f"{3*i+j}"))

sp.addRow(1)

        
print(sp)