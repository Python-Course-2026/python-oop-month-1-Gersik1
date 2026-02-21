class Circle:
    """Задача: circle"""
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return 3.14 * self.radius ** 2
        """Возвращает площадь (3.14 * r^2)"""
        pass
