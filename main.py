def calcular_pago(numero_piezas, precio_unitario):
    monto_total = numero_piezas * precio_unitario
    
    if monto_total > 500000:
        inversion_empresa = monto_total * 0.55
        prestamo_banco = monto_total * 0.30
        credito_fabricante = monto_total * 0.15
    else:
        inversion_empresa = monto_total * 0.70
        prestamo_banco = 0
        credito_fabricante = monto_total * 0.30
    
    interes_fabricante = credito_fabricante * 0.20
    total_credito_fabricante = credito_fabricante + interes_fabricante
    
    print("Número de piezas a comprar:", numero_piezas)
    print("Precio unitario de cada pieza: $", round(precio_unitario, 2))
    print("Monto total de la compra: $", round(monto_total, 2))
    print("Inversión de la empresa: $", round(inversion_empresa, 2))
    print("Préstamo del banco: $", round(prestamo_banco, 2))
    print("Crédito al fabricante (incluyendo intereses): $", round(total_credito_fabricante, 2))

numero_piezas = int(input("Ingrese el número de piezas a comprar: "))
precio_unitario = float(input("Ingrese el precio unitario de la pieza: "))
calcular_pago(numero_piezas, precio_unitario)