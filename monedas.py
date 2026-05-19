TASA_COP_DOLAR = 3890.0   
TASA_COP_EURO  = 4420.0   


def cop_a_dolar(cop):
    return cop / TASA_COP_DOLAR


def cop_a_euro(cop):
    return cop / TASA_COP_EURO


def dolar_a_cop(usd):
    return usd * TASA_COP_DOLAR


def euro_a_cop(eur):
    return eur * TASA_COP_EURO