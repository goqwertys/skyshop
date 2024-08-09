class LoggingMixin:
    def __repr__(self):
        def format_value(value):
            if isinstance(value, str):
                return f"'{value}'"
            else:
                return str(value)

        attrs = ', '.join(format_value(value) for value in self.__dict__.values())
        return f"{self.__class__.__name__}: ({attrs})"
