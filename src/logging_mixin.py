class LoggingMixin:
    def __repr__(self):
        attrs = ', '.join(str(self.__dict__.values()))
        return f"{self.__class__.__name__}: ({attrs})"
