import time

def imprimir_recuadro(texto):
  lines = texto.split('\n')
  max_length = max(len(lines) for lines in lines)
  border = '+' + '-' * (max_length +2) + '+'
  
  print(border)
  for lines in lines:
    print(f'| {lines.ljust(max_length)} |')
  print(border)
  
nombre = input("Ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
nombrecompleto = (nombre)+ " " + (apellido)

while True:
  num_uno = input("Ingrese un numero: ")
  try:
    num_float = float(num_uno)
    if num_float.is_integer():
      num_int = int(num_float)
      doble_numero = num_int * 2
      num_uno = num_int
    
    else:
      num_int = num_float
      doble_numero = num_float * 2 
      
    break
  
  except ValueError:
    print("Ingresa un numero valido")
  
  
texto = (
  f"\nBienvenido {nombrecompleto}. \nTienes {edad} años\n\n"\
  f"Ingresaste {num_int}, y el doble de {num_int} es {doble_numero}\n"
)

imprimir_recuadro(texto)

time.sleep(5)