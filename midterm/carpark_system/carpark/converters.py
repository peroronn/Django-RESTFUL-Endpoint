class FloatConverter:
    regex = r"-?\d+(\.\d+)?"  # Matches integers or floats

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
