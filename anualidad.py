import math

# 1. Anualidad compuesta de 24 períodos trimestrales vencidos, de los cuales los 4 primeros son diferidos
def ejercicio_1():
    R = 2500
    TEA = 0.36
    i = (1 + TEA) ** (1/4) - 1  # tasa de interés trimestral
    n = 20  # número de períodos después del diferimiento
    VP = R * ((1 - (1 + i) ** -n) / i)  # valor presente de la anualidad
    VP0 = VP / (1 + i) ** 4  # valor presente ajustado por los 4 períodos de diferimiento
    return round(VP0, 2)

# 2. Proceso de fabricación de una máquina con ganancias mensuales diferidas
def ejercicio_2():
    PV1 = sum([500 / (1 + 0.03) ** i for i in range(1, 6)])  # valor presente de los 5 primeros meses
    PV2 = sum([500 / (1 + 0.04) ** i for i in range(6, 30)])  # valor presente de los 24 meses posteriores
    PV2_ajustado = PV2 / (1 + 0.03) ** 5  # ajustar PV2 por el diferimiento
    return round(PV1 + PV2_ajustado, 2)

# 3. Capital necesario para cubrir las pensiones de la instrucción superior
def ejercicio_3():
    R = 200
    r = 0.20 / 12  # tasa de interés mensual
    n = 5 * 12  # 5 años, pagos mensuales
    PV = R * (1 - (1 + r) ** -n) / r  # valor presente de las anualidades
    C = PV / (1 + r) ** 3  # capital a invertir
    return round(C, 2)

# 4. Valor presente de una anualidad diferida anticipada
def ejercicio_4():
    R = 1000  # renta vencida
    i = 0.03  # tasa de interés por período
    n = 12  # número de períodos
    P = R * ((1 - (1 + i) ** -n) / i) + R * (1 + i) ** -n * (1 + i * 4) / i  # fórmula de valor presente
    return round(P, 2)

# 5. Importe de la cuota fija trimestral vencida
def ejercicio_5():
    P = 10000
    n = 2  # número de períodos
    k = 2  # períodos diferidos
    TEA = 0.40
    TET = (1 + TEA) ** (1 / 4) - 1  # tasa de interés trimestral
    R = P * (1 + TET) ** k * (TET * (1 + TET) ** n) / ((1 + TET) ** n - 1)  # cuota fija
    return round(R, 2)

# 6. Plazo diferido para percibir una renta vencida de S/.1000 mensuales durante 36 meses
def ejercicio_6():
    P = 10000
    R = 1000
    i = 0.04
    n = 36
    k = math.log((R / (P * i)) * (1 - (1 / (1 + i)) ** n)) / math.log(1 + i)
    return round(k, 2)

# 7. Plazo diferido necesario para percibir una renta mensual anticipada de S/.1,000 durante 12 meses
def ejercicio_7():
    P = 10000
    R = 1000
    i = 0.02
    n = 12
    k = math.log((R / (P * i)) * (1 - (1 / (1 + i)) ** n)) / math.log(1 + i)
    return round(k, 2)

# 8. Número de retiros mensuales posibles con un depósito inicial de S/.8,000
def ejercicio_8():
    C = 8000
    Ra = 500
    i = 0.06 / 12  # tasa de interés mensual
    valor_inicial = C * (1 + i) ** 5  # valor inicial al final del 5to mes
    n = math.log(Ra / (valor_inicial * i)) / math.log(1 + i)
    return round(n, 2)

# 9. Número de abonos mensuales para un automóvil con enganche y abonos mensuales
def ejercicio_9():
    R = 3751
    VA = 69750
    i = 0.18 / 12  # tasa de interés mensual
    n = math.log((1 - (VA * i / R)) / math.log(1 + i))
    return round(n, 2)

# 10. Tasa de interés mensual pagada por el señor Pérez
def ejercicio_10():
    R = 6000
    Ra = 1349.43
    i = 0.02  # tasa mensual aproximada
    return i

# 11. Renta perpetua mensual vencida con un valor de S/.20,000
def ejercicio_11():
    C = 20000
    TEA = 0.10
    TEM = (1 + TEA) ** (1 / 12) - 1
    R = C * TEM
    return round(R, 2)

# 12. Renta mensual perpetua con un valor presente de S/.10,000 a una TEA del 20%
def ejercicio_12():
    C = 10000
    TEA = 0.20
    TEM = (1 + TEA) ** (1 / 12) - 1
    R = C * TEM
    return round(R, 2)

# 13. Renta perpetua trimestral anticipada con un valor de S/.15,000
def ejercicio_13():
    C = 15000
    TEA = 0.08
    TET = (1 + TEA) ** (1 / 4) - 1
    R = C * (TET / (1 + TET))
    return round(R, 2)

# 14. Merced conductiva mensual anticipada por una concesión de S/.400,000
def ejercicio_14():
    C = 400000
    TEA = 0.40
    TEM = (1 + TEA) ** (1 / 12) - 1
    R = C * TEM / (1 + TEM)
    return round(R, 2)

# 15. Inversión necesaria para cubrir una renta mensual perpetua de S/.500
def ejercicio_15():
    R = 500
    TEA = 0.08
    TEM = (1 + TEA) ** (1 / 12) - 1
    P = R / TEM
    return round(P, 2)

# 16. Conversión de renta perpetua anticipada a anualidad equivalente
def ejercicio_16():
    TEM = 0.04
    R = 1000
    P = R * (1 + TEM) / TEM
    n = 20
    TEB = (1 + TEM) ** 2 - 1
    R_equivalente = P * (TEB * (1 + TEB) ** n) / ((1 + TEB) ** n - 1)
    return round(R_equivalente, 2)

# Ejecución de los ejercicios
print("Ejercicio 1:", ejercicio_1())
print("Ejercicio 2:", ejercicio_2())
print("Ejercicio 3:", ejercicio_3())
print("Ejercicio 4:", ejercicio_4())
print("Ejercicio 5:", ejercicio_5())
print("Ejercicio 6:", ejercicio_6())
print("Ejercicio 7:", ejercicio_7())
print("Ejercicio 8:", ejercicio_8())
print("Ejercicio 9:", ejercicio_9())
print("Ejercicio 10:", ejercicio_10())
print("Ejercicio 11:", ejercicio_11())
print("Ejercicio 12:", ejercicio_12())
print("Ejercicio 13:", ejercicio_13())
print("Ejercicio 14:", ejercicio_14())
print("Ejercicio 15:", ejercicio_15())
print("Ejercicio 16:", ejercicio_16())
