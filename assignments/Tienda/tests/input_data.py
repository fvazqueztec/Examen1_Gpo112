# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test Case 1
    (
        ["-1"],
        ["Número de artículos: ", 'Error en los datos'],
        ["Revisa las condiciones y mensajes cuando son datos inválidos"]
    ),
    # Test Case 2
    (
        ["1", "k"],
        ["Número de artículos: ", "Tipo de cliente: ", 'Error en los datos'],
        ["Revisa las condiciones y mensajes cuando son datos inválidos"]
    ),
    # Test Case 3
    (
        ["5", "F", "1000"],
        ["Número de artículos: ", "Tipo de cliente: ", "Total sin IVA: ",
            'Descuento: 0', 'Subtotal: 1000.0', 'IVA: 160.0', 'Total: 1160.0'],
        ["Revisa las condiciones cuando el cliente es frecuente, pero el total sin IVA no es superior a 1000"]
    ),
    # Test Case 4
    (
        ["10", "N", "1000"],
        ["Número de artículos: ", "Tipo de cliente: ", "Total sin IVA: ",
            'Descuento: 0', 'Subtotal: 1000.0', 'IVA: 160.0', 'Total: 1160.0'],
        ["Revisa las condiciones cuando el cliente es normal"]
    ),

    # Test Case 5
    (
        ["7", "F", "2150.75"],
        ["Número de artículos: ", "Tipo de cliente: ", "Total sin IVA: ",
            'Descuento: 64.52', 'Subtotal: 2086.23', 'IVA: 333.8', 'Total: 2420.03'],
        ["Revisa las condiciones cuando el cliente es frecuente, pero el total sin IVA es superior a 1000"]
    ),
]
