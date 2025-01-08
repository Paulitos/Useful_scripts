import pandas as pd
import random
import string

# Función para generar un NIF/CIF aleatorio de 9 caracteres
def generar_nif_aleatorio(_):
    # Decidir cuántas letras y dónde colocarlas
    posiciones = random.choice(["inicio", "fin", "ambos", "ninguno"])

    if posiciones == "inicio":
        return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=8))

    elif posiciones == "fin":
        return ''.join(random.choices(string.digits, k=8)) + random.choice(string.ascii_uppercase)

    elif posiciones == "ambos":
        return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=7)) + random.choice(string.ascii_uppercase)

    else:  # Ninguno
        return ''.join(random.choices(string.digits, k=9))

# Cargar el archivo Excel y seleccionar la hoja 'DATOS'
ruta_archivo = "ruta_archivo.xlsx" # Cambiar por la ruta real
with pd.ExcelWriter(ruta_archivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    df = pd.read_excel(ruta_archivo, sheet_name='DATOS')

    # Sustituir los NIF/CIF en la columna correspondiente
    columna_nif = 'CIF_NIF'  # Cambiar por el nombre real de la columna
    df[columna_nif] = df[columna_nif].astype(str).apply(generar_nif_aleatorio)

    # Guardar los cambios en la misma hoja
    df.to_excel(writer, sheet_name='DATOS', index=False)

print("Los NIF/CIF han sido anonimizados en el archivo original.")
