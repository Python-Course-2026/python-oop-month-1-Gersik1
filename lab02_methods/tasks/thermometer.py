class Thermometer:
    """Задача: thermometer"""
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32
        """(C * 9/5) + 32"""
        pass
