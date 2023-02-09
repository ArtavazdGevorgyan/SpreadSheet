from datetime import datetime


Colors = {"Black": 0,
          "Red": 1,
          "Blue": 2,
          "Yello": 3,
          "Green": 4}


class Cell:
    def __init__(self, value: str = str(), color: str = "Black") -> None:
        if isinstance(value, str):
            self.__value = value
        else:
            self.__value = str()
        self.__color = Colors[color]

    def __repr__(self):
        return str(self.__value)

    def setValue(self, val: str) -> None:
        if isinstance(val, str):
            self.__value = val

    def getValue(self) -> object:
        return self.__value

    def setColor(self, color: str) -> None:
        self.__color = Colors[color]

    def getColor(self) -> int:
        return self.__color

    def toInt(self) -> int:
        return int(self.__value)

    def toDouble(self) -> float:
        return float(self.__value)

    def toDate(self) -> datetime.date:
        return datetime.strptime(self.__value, '%m-%d-%Y').date()

    def reset(self) -> None:
        self.__value = str()
        self.__color = Colors["Black"]
