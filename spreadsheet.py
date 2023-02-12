from cell import Cell


class Spreadsheet:
    def __init__(self, row: int, col: int) -> None:
        self.__row = row
        self.__col = col
        self.spreadsheet = [[Cell() for j in range(col)] for i in range(row)]

    def __repr__(self):
        return str(self.spreadsheet)

    def setCellAt(self, row: int, col: int, cell: Cell) -> None:
        self.spreadsheet[row][col].setValue(cell.getValue())
        # self.spreadsheet[row][col].setColor(cell.getColor())

    def getCellAt(self, row: int, col: int) -> Cell:
        return self.spreadsheet[row][col]

    def addRow(self, row: int) -> None:
        self.__row += 1
        self.spreadsheet[row:row] = [[Cell() for i in range(self.__col)]]

    def removeRow(self, row: int) -> None:
        self.__row -= 1
        del self.spreadsheet[row]

    def addColumn(self, col: int) -> None:
        self.__col += 1
        for i in range(self.__row):
            self.spreadsheet[i][col:col] = [Cell()]

    def removeColumn(self, col: int) -> None:
        self.__col -= 1
        [self.spreadsheet[i].pop(col) for i in range(self.__row)]

    def swapRows(self, row1: int, row2: int) -> None:
        self.spreadsheet[row1], self.spreadsheet[row2] = \
            self.spreadsheet[row2], self.spreadsheet[row1]

    def swapColumns(self, col1: int, col2: int) -> None:
        for i in range(self.__row):
            self.spreadsheet[i][col1], self.spreadsheet[i][col2] = \
                self.spreadsheet[i][col2], self.spreadsheet[i][col1]

    def tofile(self, extention=''):
        fname = 'file.txt'
        if extention:
            fname = extention
        with open(fname, 'w') as file:
            file.write(" Row, Column: Value\n")
            for i in range(self.__row):
                for j in range(self.__col):
                    if self.spreadsheet[i][j]:
                        file.write(
                            f"{i: ^5}  {j: ^5}: {self.spreadsheet[i][j].getValue(): ^5}\n")
