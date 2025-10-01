
def conversion_f_en_c(temperature_f: float) -> float:
    temperature_c = (temperature_f-32) * 5/9
    return temperature_c


celsius = conversion_f_en_c(42.0)
print(celsius)
print(type(celsius))