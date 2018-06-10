class ChemicalSupplyStore:
    chemicals = []

    def __init__(self):
        pass

    def sort_by_price(self):
        self.chemicals.sort(key=lambda good: good.price)

    def find_by_type(self, good_type):
        found_chemicals = []

        for good in self.chemicals:
            if good.goods_type == good_type:
                found_chemicals.append(good)

        return found_chemicals

    def add_toy(self, good):
        self.chemicals += good

    def print_list(self):
        for good in self.chemicals:
            print(good)
        print("\n")

