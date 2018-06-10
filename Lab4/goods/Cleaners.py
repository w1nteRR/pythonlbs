from goods.Good import *
from enums.GoodsType import *
from enums.GoodsColour import *


class Cleaners(Good):
    goods_type = GoodsType.CLEANERS
    goods_colour = GoodsColour.BLUE

    def __init__(self, name, price, amount, id, manufacturer, goods_colour, goods_type):
        super().__init__(id, name, manufacturer, price, amount, goods_colour, goods_type)
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return "Good type: " + str(self.goods_type.value) + "  Price: " + str(self.price) + " Amount: " + str(self.amount)
