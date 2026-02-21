class Timer:
    """Задача: timer"""
    def __init__(self, sec: int):
        self.sec = sec

    def tick(self):
        while self.sec > 0:
            self.sec -= 1
        """Уменьшает sec на 1, пока > 0"""
        pass
