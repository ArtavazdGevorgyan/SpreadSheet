from cell import Cell
from spreadsheet import Spreadsheet


class Tester:
    print("Testing  Cell Results:")

    def createCell(self):
        self.cell = Cell()
        if str(self.cell) == '':
            print("Succeed: Creating Cell by Default")
        else:
            print("Failed: Creating Cell by Default")

        self.cell = Cell(5)
        if str(self.cell) == '5':
            print("Failed: passing wrong ValueType")
        else:
            print("Succeed: passing wrong ValueType")

        self.cell = Cell('test')
        if str(self.cell) == 'test':
            print("Succeed: Creating Cell by passing Values")
        else:
            print("Failed: Creating Cell by passing Values")

    def check_setValue(self):
        self.cell = Cell()
        try:
            self.cell.setValue()
            print("Failed: setValue Missing Arguments")
        except TypeError:
            print("Succeed: setValue Missing Arguments")

        self.cell.setValue(5)
        if str(self.cell) == '':
            print("Succeed: Wrong ValueType")
        else:
            print("Failed: Wrong ValueType")

        self.cell.setValue('test')
        if str(self.cell) == 'test':
            print("Succeed: setValue")
        else:
            print("Failed: setValue")

    def check_getValue(self):
        self.cell = Cell('test')
        if self.cell.getValue() == 'test':
            print("Succeed: getValue")
        else:
            print("Failed: getValue")

    def check_setColor(self):
        self.cell = Cell()
        try:
            self.cell.setColor()
            print("Failed: setColor Missing Arguments")
        except TypeError:
            print("Succeed: setColor Missing Arguments")

        try:
            self.cell.setColor("Orange")
            print("Failed: Missing Color")
        except:
            print("Succeed: Missing Color")

    def check_getColor(self):
        self.cell = Cell(color="Red")
        if self.cell.getColor() == 1:
            print("Succeed: getColor")
        else:
            print("Failed: getColor")

    def check_toInt(self):
        self.cell = Cell('test')
        try:
            self.cell.toInt()
            print("Failed: toInt passing wrong value")
        except:
            print("Succeed: toInt passing wrong value")
        self.cell = Cell('1234')
        if self.cell.toInt() == 1234:
            print("Succeed: toInt")
        else:
            print("Failed: toInt")

    def check_toDouble(self):
        self.cell = Cell('test')
        try:
            self.cell.toDouble()
            print("Failed: toDouble passing wrong value")
        except:
            print("Succeed: toDouble passing wrong value")
        self.cell = Cell('1234.3')
        if self.cell.toDouble() == 1234.3:
            print("Succeed: toDouble")
        else:
            print("Failed: toDouble")

    def check_toDate(self):
        self.cell = Cell('test')
        try:
            self.cell.toDate()
            print("Failed: toDate passing wrong value")
        except:
            print("Succeed: toDate passing wrong value")
        self.cell = Cell('12-12-3030')
        if str(self.cell.toDate()) == '3030-12-12':
            print("Succeed: toDate")
        else:
            print("Failed: toDate")

    def check_reset(self):
        self.cell = Cell('4', "Green")
        self.cell.reset()
        if self.cell.getValue() == '' and self.cell.getColor() == 0:
            print("Succeed: reset")
        else:
            print("Failed: reset")

    print("Testing Spreadsheet Results:")

    def createSpreadsheet(self):
        try:
            self.sp = Spreadsheet()
            print("Failed: Creating Spreadsheet with Missing Arguments")
        except:
            print("Succeed: Creating Spreadsheet with Missing Arguments")

        try:
            self.sp = Spreadsheet('s','v')
            print("Failed: Wrong ValueType passing")
        except:
            print("Succeed: Wrong ValueType passing")
        try:
            self.sp = Spreadsheet(5, 6)
            print("Succeed: Creating Spreadsheet by passing Values")
        except:
            print("Failed: Creating Spreadsheet by passing Values")

    def check_setCellAt(self):
        self.sp = Spreadsheet(3,4)
        try:
            self.sp.setCellAt()
            print("Failed: setCellAt Missing Arguments")
        except:
            print("Succeed: setCellAt Missing Arguments")

        try:
            self.sp.setCellAt(5,4,Cell('a'))
            print("Failed: setCellAt Index out of range")
        except:
            print("Succeed: setCellAt Index out of range")
        
        self.sp.setCellAt(1,2,Cell('a'))
        if self.sp.getCellAt(1,2).getValue()=='a':
            print("Succeed: setCellAt")
        else:
            print("Failed: setCellAt")
            
    def check_getCellAt(self):
        self.sp = Spreadsheet(3,4)
        self.sp.setCellAt(1,2,Cell('a'))
        try:
            self.sp.getCellAt(1)
            print("Failed: getCellAt Missing Arguments")
        except:
            print("Succeed: getCellAt Missing Arguments")
            
        if self.sp.getCellAt(1,2).getValue()=='a' and isinstance(self.sp.getCellAt(1,2),Cell):
            print("Succeed: getCellAt")
        else:
            print("Failed: getCellAt")

    def check_addRow(self):
        self.sp = Spreadsheet(2,3)
        for i in range(2):
            for j in range(3):
                self.sp.setCellAt(i,j,Cell(f"{3*i+j}"))
        try:
            self.sp.addRow()
            print("Failed: addRow Missing Argument")
        except:
            print("Succeed: addRow Missing Argument")
            
        self.sp.addRow(1)
        
            
            
        
        
test = Tester()
test.check_getCellAt()
