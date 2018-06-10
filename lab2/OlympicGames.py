class OlympicGames:
    objects = []

    def __init__(self):
        pass

    def sort_by_capacity(self):
        self.objects.sort(key=lambda object: object.capacity)

    def find_by_type(self, sport_type):
        found_objects = []
        for object in self.objects:
            if object.sport_type == sport_type:
                found_objects.append(object)

        return found_objects

    def add_object(self, object):
        self.objects += object

    def print_list(self):
        for object in self.objects:
            print(object)
        print("\n")