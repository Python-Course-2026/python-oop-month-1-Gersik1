class PasswordChecker:
    """Задача: password_checker"""
    def __init__(self, pwd: str):
        self.pwd = pwd

    def is_strong(self) -> bool:
        if len(self.pwd) >= 8 and any(ch.isdigit() for ch in self.pwd):
            return True
        """Длина >= 8 и есть цифра"""
        pass
