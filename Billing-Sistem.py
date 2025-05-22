#entrada
# centramos el texto y lo ponemos en negrita
texto = "OLIMPICA S.A"
texto_2 = "NIT: 34829340573-3"
ancho_terminal = 50  # Ancho total del campo donde se centrará el texto
negrita = "\033[1m"  # Secuencia ANSI para activar la negrita
reset = "\033[0m"  # Secuencia ANSI para restablecer el formato

# Centramos el texto en el ancho especificado y le aplicamos negrita
texto_formateado = f"{negrita}{texto.center(ancho_terminal)}{reset}"
texto_nit = f"{negrita}{texto_2.center(ancho_terminal)}{reset}"

# Imprimimos el texto formateado y agregamos datos para simular factura de la olimpica
print(texto_formateado)
print("STO       SIMON      BOLIVAR          CALLE       6B     #18-    20")
print(texto_nit)
print("             ¡DONDE LA CALIDAD NO CUESTA MAS!"           )
print("GERENTE: MARTHA GARCIA")
print("TELEFONOS: 3109863241- 3045678932")
print("FECHA DE EXPEDICION: 18-07-25")

nombre_del_producto = input ("ingrese el nombre del producto:").strip().lower()

    #desarrollo
# hacemos un bucle para que en caso de ingresar valores negativos el programa no se frene 
#en los numeros positivos no incluimos el cero porque necesitamos que se compre algo para hacer una factura
while True:
        try:
            cantidad_de_producto = int(input("Ingrese la cantidad de producto: "))
            if cantidad_de_producto >0:
                break  # Sale del bucle si el número es positivo mayor a 0
            else:
                print("La cantidad de producto debe ser número positivo mayor a 0.")
        except ValueError: #queremos convertir los datos de entrada a lo que pedimos especificamente sin frenar el programa
            print("Por favor, ingrese un número entero válido.")

while True:
        try:
            valor_unitario = float(input("ingrese el valor unitario:"))
            if valor_unitario >0:
                break # sale del bucle si el valor es positivo mayor a 0
            else:
                print ("el valor unitario debe ser positivo mayor a 0.")
        except ValueError:
            print("por favor, ingrese valor positivo mayor a 0.")
# antes de definir la variable descuento, necesitamos saber si existe o no uno. en caso de que la respuesta no sea la esperada, preguntar hasta obtenerla
while True:
        posible_descuento = input("ingrese si aplica descuento (si/no):").strip().lower()
        if posible_descuento == "si" or posible_descuento == "no":
            break
        else:
            print("debe ingresar si aplica descuento o no")

if posible_descuento == "si": #al existir dos opciones, deben existir tambien dos caminos a seguir
            while True:
                try:
                    descuento = float(input("ingrese el valor del descuento (0-100): "))
                    if 0<= descuento <=100:
                        break #sale del bucle si el descuento esta entre los valores permitidos
                    else:
                        print("el descuento debe estar entre el rango 0-100")
                except ValueError: #si no se ingresa un numero debe verificar el error
                        print("por favor, ingrese un caracter valido.")
else:
                descuento = 0 #en caso de no existir descuento le agregamos el valor de cero


#definimos las variables para realizar las operaciones matematicas correspondientes
total_de_la_compra = cantidad_de_producto * valor_unitario
compra_con_descuento = total_de_la_compra - (total_de_la_compra * descuento)/100
   
    #salida
print(f"el nombre de producto es: {nombre_del_producto}")
print(f"la cantidad de producto: {cantidad_de_producto}")
print(f"el valor unitario es: {valor_unitario:.2f}")
print(f"el valor total de la compra es: {total_de_la_compra:.2f}")

if posible_descuento == "si": 
    print(f"el valor con el descuento es: {compra_con_descuento:.2f} descuento aplicado: {descuento:.2f} % ")
else: 
    print("no aplica descuento")
print("                                 ¡GRACIAS POR PREFERIRNOS!                                                 ")