"""
POrnsawan Khareram
68304015-9
"""

from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @abstractmethod
    def get_purpose(self):
        pass

    @abstractmethod
    def get_recommended_lighting(self):
        pass

    def calculate_area(self):
        return self.length * self.width

    def describe_room(self):
        area = self.calculate_area()
        return f"A {self.__class__.__name__} of {area} sq ft used for {self.get_purpose()}"


class Bedroom(Room):
    def __init__(self, length, width, bed_size):
        super().__init__(length, width)
        self.bed_size = bed_size

    def get_purpose(self):
        return f"sleeping and relaxation (bed size: {self.bed_size} ft)"

    def get_recommended_lighting(self):
        return 15


class Kitchen(Room):
    def __init__(self, length, width, has_island=True):
        super().__init__(length, width)
        self.has_island = has_island

    def get_purpose(self):
        if self.has_island:
            return "cooking and food preparation with an island"
        return "cooking and food preparation"

    def get_recommended_lighting(self):
        return 35

    def calculate_counter_space(self):
        """
        Calculate Kitchen Area

        Parameters
        ------
        nothing

        Return
        ------
        tuple(float, float)
              island_countrer_area is of the island counter area in square feet
              wall_counter is area of wall counter in frrt
        Reises
        ------
        nothing

        Example
        ------
        >>> obj.calculate_counter_space()
        (13.0, 25.76)

        """

        room_area = self.calculate_area()
        if self.has_island:
            island_counter = room_area / 5
            wall_counter = room_area / 4
        else:
            island_counter = 0
            wall_counter = room_area / 2
        return island_counter, wall_counter

