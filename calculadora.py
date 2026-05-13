"----------------------------------------------"
"Calculadora mejorada con funciones y manejo de excepciones"
    
# --- Funciones de Operacion ---

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Manejo de excepcion especifica para division por cero
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b

# --- Cuerpo Principal del Programa ---

def calculadora():
    print("\n--- CALCULADORA PYTHON ---")
    try:
        # Intentamos convertir las entradas a float
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("Introduce el segundo numero: "))
        operacion = input("Introduce la operacion (+, -, *, /): ")

        if operacion == '+':
            resultado = sumar(num1, num2)
        elif operacion == '-':
            resultado = restar(num1, num2)
        elif operacion == '*':
            resultado = multiplicar(num1, num2)
        elif operacion == '/':
            resultado = dividir(num1, num2)
        else:
            print("Operacion invalida.")
            return

        print(f"El resultado es: {resultado}")

    except ValueError:
        # Se ejecuta si el usuario ingresa letras en lugar de numeros
        print("Error: Por favor, introduce solo valores numericos.")
    except ZeroDivisionError as e:
        # Se ejecuta si ocurre la division por cero
        print(f"Error: {e}")
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrio un error inesperado: {e}")

# Ejecutamos la calculadora
if __name__ == '__main__': calculadora()
calculadora()
