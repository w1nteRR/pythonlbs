from goods.Good import *
from enums.GoodsType import *
from enums.GoodsColour import *


class LaundryDetergents(Good):
    goods_type = GoodsType.LAUNDRY_DETERGENTS
    goods_colour = GoodsColour.BLACK

    def __init__(self, name, price, amount, smell, volume, id, manufacturer, goods_colour, goods_type):
        super().__init__(id, name, manufacturer, price, amount, goods_colour, goods_type)
        self.name = name
        self.price = price
        self.amount = amount
        self.smell = smell
        self.volume = volume

    def __str__(self):
        return "Good type: " + str(self.goods_type.value) + "  Smell: " + self.smell + " Volume: " + str(
            self.volume)
