from cell import Cell
import numpy as np


class Spreadsheet:
    def __init__(self, row: int, col: int) -> None:
        self.spredsheet = np.empty(shape=(row, col), dtype=Cell)

    def __repr__(self):
        return str(self.spredsheet)

    def setCellAt(self, row: int, col: int, cell: Cell) -> None:
        self.spredsheet[row, col] = cell

    def getCellAt(self, row: int, col: int) -> Cell:
        return self.spredsheet[row, col]

    def addRow(self, row: int) -> None:
        self.spredsheet = np.insert(self.spredsheet, (row,),
                                    Cell(" "), axis=0)   # Fake a arac, chhavatal

    def removeRow(self, row: int) -> None:
        self.spredsheet = np.delete(self.spredsheet, (row,), axis=0)

    def addColumn(self, col: int) -> None:
        self.spredsheet = np.insert(self.spredsheet, (col,),
                                    Cell(" "), axis=1)  # Nuynn el stex

    def removeColumn(self, col: int) -> None:
        self.spredsheet = np.delete(self.spredsheet, (col,), axis=1)

    def swapRows(self, row1: int, row2: int) -> None:
        self.spredsheet[[row1, row2]] = self.spredsheet[[row2, row1]]

    def swapColumns(self, col1: int, col2: int) -> None:
        self.spredsheet[:, [col1, col2]] = self.spredsheet[:, [col2, col1]]
