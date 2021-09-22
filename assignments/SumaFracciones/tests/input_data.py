# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["-5"],
        # Outputs
        ["Escribe un numero: ", "Error en los datos"],
        # Message in case of failure
        "Revisa los mensajes cuando el numero es negativo o cero"
    ),
    # Test case 2
    (
        # Inputs
        ["6"],
        # Outputs
        ["Escribe un numero: ", "2.45"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado"
    ),
    # Test case 3
    (
        # Inputs
        ["7"],
        # Outputs
        ["Escribe un numero: ", "2.5929"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado y el redondeo a 4 digitos"
    ),
]
