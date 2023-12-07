class Sports:
    def __init__(self,name):
        self._name=name

    @property
    def sports_name(self):
        return self._name
        
    @sports_name.setter
    def sports_name(self,value):
        self._name=value

    def practice(self):
        print_str = "Doing Sports practice"
        return print_str

class LandSports(Sports):
    def __init__(self, name,field):
        super().__init__(name)
        self._field=field

    @property
    def landsports_field(self):
        return self._field

    def practice(self):
        print_str = "Doing Land Sports practice"
        return print_str


class WaterSports(Sports):
    def __init__(self, name,activity):
        super().__init__(name)
        self._activity=activity
    @property
    def watersports_activity(self):
        return self._activity
    
    def practice(self):
        print_str = "Doing Water Sports practice"
        return print_str

class BallSports(LandSports):
    def __init__(self, name):
        super().__init__(name)

class NonBallSports(LandSports):
    def __init__(self, name):
        super().__init__(name)

class PoolSports(WaterSports):
    def __init__(self, name):
        super().__init__(name)

class SeaSports(WaterSports):
    def __init__(self, name):
        super().__init__(name)


if __name__=="__main__":
    baseball=LandSports("baseball", "diamond field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    print(baseball.practice())

    water_sliing=WaterSports("Water Skiing","Ride the waves and feel the splash of water on your face as you carve through the surf.")
    print(water_sliing.sports_name)
    print(water_sliing.watersports_activity)
    print(water_sliing.practice())

    sports=Sports("Softball")
    print(sports.sports_name)
    print(sports.practice())