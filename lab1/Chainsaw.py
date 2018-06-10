class Chainsaw:
    totalPower = 0
    
    def __init__(self, brand="Still", type="Fuel", engineValue=0.55, weight=5.65, power=2.4):
                
        self.brand = brand 
        self.type = type
        self.engineValue = engineValue
        self.weight = weight
        self.power = power
        Chainsaw.totalPower += power

    def to_string(self):
        print(" Name: " + self.brand + " Type:", self.type,
            " Engine value:", self.engineValue, " Weight:", self.weight, " Power:", self.power)

    def print_power(self):
        print(" Chainsaw" + self.brand, " has power", self.power)
    
    @staticmethod 
    def print_static_power():
        print("Total power: ", Chainsaw.totalPower)
        
if __name__ == '__main__':
    chainsaw_werk = Chainsaw("Werk", "Electric", 0.40, 4.5, 2.2)
    chainsaw_still = Chainsaw()
    chainsaw_bosch = Chainsaw("Bosch", "Fuel", 0.45, 4.6, 2.1)

    print("\n")

    chainsaw_werk.to_string()
    chainsaw_still.to_string()
    chainsaw_bosch.to_string()

    print("\n")
    chainsaw_werk.print_power()
    chainsaw_still.print_power()
    chainsaw_bosch.print_power()

    print("\n")
    Chainsaw.print_static_power()
