# pylint: disable-msg=E0611
from objects.BiathlonCenter import *
from objects.HockeyCenter import *
from OlympicGames import *
from objects.IndoorcleRink import *
from objects.SkiJumpingCenter import *
from objects.SlidingCenter import *

if __name__ == '__main__':
    ind = OlympicGames()

    biathlon = BiathlonCenter(10, "Patrick Stadium", 10200, "South Corea")
    hockey = HockeyCenter(10, "Sd", 8300, "USA")
    curling = IndoorcleRink(4, "klk", 3232, "China")
    skiJumping = SkiJumpingCenter(15, "vnm", 4000, "Finland")
    skeleton = SlidingCenter(32, "dad", 4000, "South Corea")

    ind.objects = [biathlon, hockey, curling, skiJumping, skeleton]
    print("Initial list:")
    ind.print_list()

    ind.sort_by_capacity()
    print("Sorted list")
    ind.print_list()

    ind.objects = ind.find_by_type(SportType.HOCKEY)
    print("Found list:")
    ind.print_list()

    pass