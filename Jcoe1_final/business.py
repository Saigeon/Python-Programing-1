#! /user/bin/env python3
from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Item:
    itemID:int = 0
    itemName:str = ""
    itemEnd:str = ""
    itemStart:str = ""

    @property
    def timeRemaining(self):
        expirationDate = date(self.itemEnd)
        now = datetime.now()
        currentDate = datetime(now.year, now.month, now.day)
        result = abs(currentDate-expirationDate).days
        return result

class Shelf:
    def __init__(self):
        self.__list = []

    def add(self, item):
        return self.__list.append(item)

    def remove(self, number):
        return self.__list.pop(number-1)

    def get(self, number):
        return self.__list[number]

    def __iter__(self):
        for item in self.__list:
            yield item

def main():
    pass

if __name__ == "__main__":
    main()
