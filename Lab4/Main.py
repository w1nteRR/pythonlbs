from goods.Cleaners import *
from goods.AirFresheners import *
from ChemicalSupplyStore import *
from goods.InsectRepellents import *
from goods.LaundryDetergents import *
from goods.Liquids import *
from goods.Powders import *
from goods.ScouringPads import *

if __name__ == '__main__':
    shop = ChemicalSupplyStore()

    airFreshener = AirFresheners("Air Fresh Matic", 4.2, 5, "Fu", 10.0)
    cleaner = Cleaners("Kitchen", 5.2, 3)
    insectRepellent = InsectRepellents("Lol", 5.2, 5, "Fu", 12.0)
    laundryDetergent = LaundryDetergents("LALA", 4.8, 5, "Fu", 12.5)
    liquids = Liquids("Fairy", 5.3, 3, "ds", 10.0)
    powders = Powders("Tide", 3.6, 4, "Polyphosphoric acid", 10.9)
    scouringPad = ScouringPads("Kuhovarochka", 6.6, 3, "fafa", 15.5)

    shop.chemicals = [airFreshener, cleaner, insectRepellent, laundryDetergent, liquids, powders, scouringPad]
    print("Initial list:")
    shop.print_list()

    shop.sort_by_price()
    print("Sorted list")
    shop.print_list()

    shop.chemicals = shop.find_by_type(GoodsType.SCOURING_PADS)
    print("Found list:")
    shop.print_list()

    pass
