# load_cars_to_hbase.py
# Autor: Liceth Mendez
# Descripción: Script para cargar datos desde un archivo CSV a HBase usando HappyBase.

import happybase
import pandas as pd

# Configuración de conexión a HBase Thrift Server
connection = happybase.Connection('localhost')
connection.open()

# Definición de la tabla
TABLE_NAME = 'car_details'

# Familias de columnas
column_families = {
    'info': dict(),          # Información general del carro
    'details': dict(),       # Detalles adicionales
}

# Eliminar la tabla si ya existe para recrearla
tables = connection.tables()
if TABLE_NAME.encode() in tables:
    print(f"Eliminando tabla existente {TABLE_NAME}...")
    connection.delete_table(TABLE_NAME, disable=True)

# Crear tabla
print(f"Creando tabla {TABLE_NAME}...")
connection.create_table(TABLE_NAME, column_families)

# Leer el CSV
print("Leyendo archivo CSV...")
df = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')

# Cargar los datos a HBase
print("Cargando datos a HBase...")
table = connection.table(TABLE_NAME)

for idx, row in df.iterrows():
    key = str(idx)  # Puedes usar otro campo como 'id' si existe
    table.put(key, {
        b'info:name': str(row['name']).encode(),
        b'info:year': str(row['year']).encode(),
        b'info:selling_price': str(row['selling_price']).encode(),
        b'info:km_driven': str(row['km_driven']).encode(),
        b'details:fuel': str(row['fuel']).encode(),
        b'details:seller_type': str(row['seller_type']).encode(),
        b'details:transmission': str(row['transmission']).encode(),
        b'details:owner': str(row['owner']).encode(),
    })

print("Datos cargados exitosamente.")

# Cerrar la conexión
connection.close()
