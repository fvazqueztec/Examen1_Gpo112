![Tec de Monterrey](../../images/logotecmty.png)
# Tienda

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe aquí tu código
    

if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

El siguiente algoritmo se puede usar para determinar la cantidad a pagar en un tienda, considerando lo siguiente:

   * Solicitar el numero de artículos, si el número de articulos es cero o menor que cero, el sistema deberá terminar y mostrar el mensaje "Error en los datos" 
   * Solicitar el total sin IVA,  si el total sin IVA es cero o menor que cero, el sistema deberá terminar y mostrar el mensaje "Error en los datos" 
   * Solicitar el tipo de cliente: "F" es frecuente o "N" es normal, si el tipo de cliente es diferente a 'F' o a 'N', el sistema deberá terminar y mostrar el mensaje "Error en los datos"
   * Si el cliente es Normal (N) no existe descuento, por lo que se deberá mostrar "Descuento: 0" (ver ejemplo 3)
   * Si el cliente es Frecuente (F) y el total sin IVA es mayor que 1000 pesos, entonces se realiza un 3% de descuento, el sistema deberá mostrar el descuento, la cantidad se deberá redondear a 2 decimales y el subtotal a 2 decimales. Recuerda utilizar la instrucción round(cantidad, 2)
   * Se calcula el IVA 16%, se muestra el IVA (redondear a 2 decimales) y el total a pagar ya con IVA incluido (redondear a 2 decimales). Recuerda utilizar la instrucción round(cantidad, 2)

   
**Entradas**  
Número de artículos
Total sin IVA (solo si el número de artículos es mayor que 0)
Tipo de cliente (solo si el total sin iva es mayor que 0)

  
**Salidas**  
Si el número de artículos es menor o iugual a 0, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Si el total sin IVA es menor o iugual a 0, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Si el tipo de cliente es diferente a F o N, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Descuento, en caso de existir
IVA
Total 

## Ejemplos  

Ejemplo 1    

```plaintext
Número de artículos: 0
Error en los datos
```

Ejemplo 2

```plaintext
Número de artículos: 5
Tipo de cliente: J
Error en los datos
```

Ejemplo 3

```plaintext
Número de artículos: 5
Tipo de cliente: N
Total sin IVA: 400
Descuento: 0
Subtotal: 400.0
IVA: 64.0
Total: 464.0
```

Ejemplo 4
```plaintext
Número de artículos: 7
Tipo de cliente: F
Total sin IVA: 1505.76
Descuento: 45.17
Subtotal: 1460.59
IVA: 233.69
Total: 1694.28
```



**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.
